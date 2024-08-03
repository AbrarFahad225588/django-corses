from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return  HttpResponse("the is app courses page")
def about(request):
    return  HttpResponse("the is app about page")
def home(request):
    return  HttpResponse("the is app home page")
