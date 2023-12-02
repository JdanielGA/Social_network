''' Core views '''
## Path: social_network/core/views.py
# Desc: Modules and libraries for views.
from django.shortcuts import render
from django.http import HttpResponse


# Desc: Index view.
def index(request):
    return render(request, 'index.html')
