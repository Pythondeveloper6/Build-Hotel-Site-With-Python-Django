from django.shortcuts import render

# Create your views here.
from .models import About

def aboutus(request):
    about = About.objects.last()
    template = 'about/about.html'
    context = {
        'about' : about 
    }

    return render(request , template , context)