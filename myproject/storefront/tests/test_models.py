from django.test import TestCase
from ..models import Person, Location, JobTitle, Skill

class ModelTestCase(TestCase):

    def setUp(self):
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

    def test_person_creation(self):
        self.assertEqual(self.person.first_name, "Alice")
        self.assertEqual(self.person.last_name, "Eden")
        self.assertEqual(self.person.age, 45)
        self.assertEqual(self.person.location.city, "New York")
        self.assertEqual(self.person.location.country, "USA")
        self.assertEqual(self.person.job_title.title, "Data Engineer")
        self.assertIn(self.skill, self.person.skills.all())

    def test_string_representation(self):
        self.assertEqual(str(self.person), "Alice Eden")
        self.assertEqual(str(self.location), "New York, USA")
        self.assertEqual(str(self.job_title), "Data Engineer")
        self.assertEqual(str(self.skill), "Python")
