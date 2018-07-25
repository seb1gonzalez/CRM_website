
from django.shortcuts import render

def homepage(request):
    return render(request,'index.html')
def services(request):
    return render(request,'services.html')
def ourTeam(request):
    return render(request,'our_team.html')
def contact(request):
    return render(request,'contact.html')
