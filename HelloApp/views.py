from django.shortcuts import render

# Create your views here.
from  django.http import  HttpResponse
def Hello(request):
    return HttpResponse("Hello World!I am coming..…")

