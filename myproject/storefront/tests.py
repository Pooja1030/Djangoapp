from django.test import TestCase
from .models import Person, Location, JobTitle, Skill
from django.urls import resolve,reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from .serializers import PersonSerializer
from .views import PersonList, PersonDetail


# Model test case

class ModelTestCase(TestCase):

    def setUp(self):
        self.location = Location.objects.create(city="Washington", country="USA")
        self.job_title = JobTitle.objects.create(title="Data Engineer")
        self.skill = Skill.objects.create(name="Python")
        self.person = Person.objects.create(
            first_name = "Alice",
            last_name="Eden",
            age=45,
            location=self.location,
            job_title = self.job_title,
        )
        self.person.skills.add(self.skill)

    def test_person_creation(self):
        person = self.person
        self.assertEqual(person.first_name, "Alice")
        self.assertEqual(person.last_name, "Eden")
        self.assertEqual(person.age, 45)
        self.assertEqual(person.location.city, "Washington")
        self.assertEqual(person.location.country, "USA")
        self.assertEqual(person.job_title.title, "Data Engineer")
        self.assertIn(self.skill, person.skills.all())

    def test_string_representation(self):
        self.assertEqual(str(self.person), "Alice Eden")
        self.assertEqual(str(self.location), "Washington, USA")
        self.assertEqual(str(self.job_title), "Data Engineer")
        self.assertEqual(str(self.skill), "Python")


# View Tests

class ViewTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.location = Location.objects.create(city="Washington", country="USA")
        self.job_title = JobTitle.objects.create(title="Data Engineer")
        self.skill = Skill.objects.create(name="Python")
        self.person = Person.objects.create(
            first_name = "Alice",
            last_name = "Eden",
            age=45,
            location = self.location,
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
        response = self.client.get(reverse('person-detail', kwargs={'id':self.person.id}))
        person = Person.objects.get(id=self.person.id)
        serializer = PersonSerializer(person)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_create_person(self):
        data = {
            'first_name': 'Alice',
            'last_name' : 'Eden',
            'age' : 45,
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
            'last_name' : 'Hesengberg',
            'age' : 45,
            'location': self.location.id,
            'job_title': self.job_title.id,
            'skills': [self.skill.id]
        }
       
        response = self.client.put(reverse('person-detail', kwargs={'id': self.person.id}), data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.person.refresh_from_db()
        self.assertEqual(self.person.last_name, 'Hesengberg')

    
    def test_delete_person(self):
        response = self.client.delete(reverse('person-detail', kwargs={'id': self.person.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Person.objects.filter(id=self.person.id).exists())
        



# URL Tests

class UrlsTestCase(TestCase):

    def test_person_list_url(self):
        url = reverse('person-list')
        self.assertEqual(resolve(url).func.view_class, PersonList)

 
    def test_person_detail_url(self):
        url = reverse('person-detail', kwargs={'id':1})
        self.assertEqual(resolve(url).func.view_class, PersonDetail)
