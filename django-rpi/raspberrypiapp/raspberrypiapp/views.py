
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def homepage(request):

    return render(request,'pages/index.html')

