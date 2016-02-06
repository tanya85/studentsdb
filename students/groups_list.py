from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Views for Groups

def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')


