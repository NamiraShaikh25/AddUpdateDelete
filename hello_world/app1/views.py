from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return render(request,'a.html',{'titles':'django','link':'http://127.0.0.1:8000/'})
def profile(request):
    return render(request,'a.html',{'titles':'pppppp','link':'http://127.0.0.1:8000/'})