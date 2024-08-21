from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSerializer
from .db_connection import db
from bson import ObjectId

person_collection = db['storefront']

class PersonList(APIView):
    def get(self, request):
        persons = person_collection.find()
        persons_list = []
        for person in persons:
            person['id'] = str(person.pop('_id'))
            persons_list.append(person)
        serializer = PersonSerializer(persons_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            person_collection.insert_one(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonDetail(APIView):
    def get(self, request, id):
        person = person_collection.find_one({"_id": ObjectId(id)})
        if person:
            person['id'] = str(person.pop('_id'))
            serializer = PersonSerializer(person)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            person_collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": data}
            )
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        result = person_collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count > 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)







# from django.shortcuts import render, redirect, get_object_or_404
# from .models import person_collection
# from django.http import HttpResponse
# from .db_connection import db
# from bson import ObjectId
# # Create your views here.

# person_collection = db['storefront']

# def index(request):
#     return HttpResponse("<h1>App is running successfully</h1>")


# def add_person(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         age = request.POST.get('age')
#         records = {
#         "first_name" : first_name,
#         "last_name" : last_name,
#         "age" : age
#         }
#         person_collection.insert_one(records)
#         return redirect('get_all_person') 
#     return render(request, 'add_person.html')


# # Reading the data
# def get_all_person(request):
#     persons = person_collection.find()
#     persons_list = []
#     for person in persons:
#         # Convert ObjectId to string for use in URLs
#         person['id'] = str(person.pop('_id'))
#         persons_list.append(person)
#     return render(request, 'show_all_person.html', {'persons': persons_list})

# # Update
# def update_person(request, id):
#     person = person_collection.find_one({"_id": ObjectId(id)})
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         age = request.POST.get('age')
#         person_collection.update_one(
#             {"_id": ObjectId(id)},
#             {"$set": {"first_name": first_name, "last_name": last_name, "age": age}}
#         )
#         return redirect('get_all_person')
#     return render(request, 'update_person.html', {'person': person})
# # deleting the data

# def delete_person(request, id):
#     if request.method == 'POST':
#         person_collection.delete_one({"_id": ObjectId(id)})
#         return redirect('get_all_person')
#     person = person_collection.find_one({"_id": ObjectId(id)})
#     return render(request, 'delete_person.html', {'person': person})


