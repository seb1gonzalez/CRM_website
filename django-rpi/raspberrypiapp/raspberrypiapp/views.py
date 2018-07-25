
from django.shortcuts import render

def homepage(request):
    return render(request,'index.html')
def services(request):
    return render(request,'templates/services.html')
def ourTeam(request):
    return render(request,'templates/our_team.html')
def contact(request):
    return render(request,'templates/contact.html')
