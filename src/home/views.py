from django.shortcuts import render
from property.models import Property , Category
from agents.models import Agent
from django.db.models import Count
# Create your views here.


def home(request):
    category_list = Category.objects.annotate(property_count=Count('property')).values('category_name' , 'property_count' , 'image')
    print(category_list)
    property_list = Property.objects.all()
    agent_list = Agent.objects.all()
    template = 'home/home.html'
    context = {
        'category_list_home' : category_list ,
        'property_list_home' : property_list ,
        'agent_list_home' : agent_list
    }

    return render(request , template , context)