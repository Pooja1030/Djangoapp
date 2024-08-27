from rest_framework import serializers
from .models import Person, Location, JobTitle, Skill

# Created Location, JobTitle, Skill serializer and updated the PersonSerializer

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
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())
    job_title = serializers.PrimaryKeyRelatedField(queryset=JobTitle.objects.all())
    skills = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True)

    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'age', 'location', 'job_title', 'skills']
