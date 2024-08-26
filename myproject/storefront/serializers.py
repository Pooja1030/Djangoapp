from rest_framework import serializers
from .models import Person, Location, JobTitle, Skill

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    job_title = JobTitleSerializer()
    skills = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True)
    

    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'age', 'location', 'job_title', 'skills']
