# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
  # return HttpResponse("Hello world! This is homepage.")
  return render(request, 'home.html')

def about(request):
  # return HttpResponse("This is about page")
  return render(request, 'about.html')
