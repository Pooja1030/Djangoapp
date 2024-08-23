# from rest_framework import serializers
# from .models import Person

# class PersonSerializer(serializers.Serializer):
#     id = serializers.CharField(read_only=True)
#     first_name = serializers.CharField(required=True)
#     last_name = serializers.CharField(required=True)
#     age = serializers.IntegerField(required=True)



from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'age']
