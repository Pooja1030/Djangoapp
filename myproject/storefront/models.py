from django.db import models

# Location model -- includes city and country
class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.country}"


# JobTitle model -- includes title of the job
class JobTitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title



# Skill model -- includes skill name 
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Person model -- includes the details of the person
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    job_title = models.ForeignKey(JobTitle, on_delete=models.SET_NULL, null=True)
    skills = models.ManyToManyField(Skill, blank=True)



    def __str__(self):
        return f"{self.first_name} {self.last_name}"
