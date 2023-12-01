''' Core urls '''
## Path: social_network/core/urls.py
# Desc: Modules and libraries for urls.
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]