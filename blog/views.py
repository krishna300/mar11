from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def home(request):
     return HttpResponse("hi iango")

    
def index(request):
     return HttpResponse("hi Index from blog urls")