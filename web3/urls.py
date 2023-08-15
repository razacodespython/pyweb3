from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store_number', views.store_number, name='store_number'),
    path('retrieve_number', views.retrieve_number, name='retrieve_number'),
    path('add_person', views.add_person, name='add_person'),
    path('retrieve_person_number', views.retrieve_person_number, name='retrieve_person_number'),
]