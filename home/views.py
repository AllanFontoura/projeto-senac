from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return render(request, 'home.html')


