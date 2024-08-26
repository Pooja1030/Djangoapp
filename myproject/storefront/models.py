# from django.db import models
# from .db_connection import db

# # Create your models here.
# person_collection = db['storefront']

from django.db import models


# Created Location, JobTitle, Skill Model

class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.country}"


class JobTitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    job_title = models.ForeignKey(JobTitle, on_delete=models.SET_NULL, null=True)
    skills = models.ManyToManyField(Skill, blank=True)



    def __str__(self):
        return f"{self.first_name} {self.last_name}"
