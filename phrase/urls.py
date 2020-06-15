# Django libs
from django.urls import path

# Our libs
from . import views

urlpatterns = [
    path('', views.index, name='index')
]