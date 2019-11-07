from django.shortcuts import render, HttpResponse, reverse, redirect
from django.contrib import auth, messages

def home(request):
    return render(request, 'home.template.html')