from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("welcome to emobilis")

def about(request):
    return HttpResponse("about emobilis")