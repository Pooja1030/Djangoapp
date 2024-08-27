from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSerializer
from .models import Person


# PersonList - Get and Post method

class PersonList(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# PersonDetail -- Put, Delete, Get all details
class PersonDetail(APIView):
    def get(self, request, id):
        try:
            person = Person.objects.get(id=id)
            serializer = PersonSerializer(person)
            return Response(serializer.data)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            person = Person.objects.get(id=id)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            person = Person.objects.get(id=id)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


