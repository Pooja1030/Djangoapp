from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from ..models import Person, Location, JobTitle, Skill
from ..serializers import PersonSerializer

class ViewTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.location = Location.objects.create(city="New York", country="USA")
        self.job_title = JobTitle.objects.create(title="Data Engineer")
        self.skill = Skill.objects.create(name="Python")
        self.person = Person.objects.create(
            first_name="Alice",
            last_name="Eden",
            age=45,
            location=self.location,
            job_title=self.job_title,
        )
        self.person.skills.add(self.skill)

    def test_get_all_persons(self):
        response = self.client.get(reverse('person-list'))
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_person(self):
        response = self.client.get(reverse('person-detail', kwargs={'id': self.person.id}))
        person = Person.objects.get(id=self.person.id)
        serializer = PersonSerializer(person)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_person(self):
        data = {
            'first_name': 'Alice',
            'last_name': 'Eden',
            'age': 45,
            'location': self.location.id,
            'job_title': self.job_title.id,
            'skills': [self.skill.id]
        }

        response = self.client.post(reverse('person-list'), data, format='json')
        print(response.data) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        

    def test_update_person(self):
        data = {
            'first_name': 'Alice',
            'last_name': 'Smith',
            'age': 45,
            'location': self.location.id,
            'job_title': self.job_title.id,
            'skills': [self.skill.id]
        }

        response = self.client.put(reverse('person-detail', kwargs={'id': self.person.id}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.person.refresh_from_db()
        self.assertEqual(self.person.last_name, 'Smith')

    def test_delete_person(self):
        response = self.client.delete(reverse('person-detail', kwargs={'id': self.person.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Person.objects.filter(id=self.person.id).exists())
