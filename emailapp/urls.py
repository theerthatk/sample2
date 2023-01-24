from django.urls import path
from .views import *

urlpatterns=[
    path('register/',register),
    path('contact/',contact),
    path('regis/',regis)
]