from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "index.html")

def about(request):
    names = ["Shohan", "Arup", "Shammo"]
    return render(request, 'about.html', context={'names': names})


 