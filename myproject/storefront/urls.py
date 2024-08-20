# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('add/', views.add_person, name='add_person'),
#     path('show/', views.get_all_person, name='get_all_person'),
#     path('update/<str:id>/', views.update_person, name='update_person'),
#     path('delete/<str:id>/', views.delete_person, name='delete_person'),
# ]

from django.urls import path
from .views import PersonList, PersonDetail

urlpatterns = [
    path('api/persons/', PersonList.as_view(), name='person-list'),  # List and Create
    path('api/persons/<str:id>/', PersonDetail.as_view(), name='person-detail'),  # Retrieve, Update, and Delete
]

