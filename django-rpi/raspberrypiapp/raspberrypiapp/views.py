
from django.shortcuts import render

def homepage(request):
    return render(request,'pages/index.html')
def services(request):
    return render(request,'pages/services.html')
def ourTeam(request):
    return render(request,'pages/our_team.html')
def contact(request):
    return render(request,'pages/contact.html')
