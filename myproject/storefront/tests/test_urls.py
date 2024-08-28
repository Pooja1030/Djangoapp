from django.test import TestCase
from django.urls import resolve, reverse
from ..views import PersonList, PersonDetail

class UrlsTestCase(TestCase):

    def test_person_list_url(self):
        url = reverse('person-list')
        self.assertEqual(resolve(url).func.view_class, PersonList)

    def test_person_detail_url(self):
        url = reverse('person-detail', kwargs={'id': 1})
        self.assertEqual(resolve(url).func.view_class, PersonDetail)
