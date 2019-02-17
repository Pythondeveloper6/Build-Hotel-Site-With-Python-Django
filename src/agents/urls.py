from django.urls import path
from . import views


app_name = 'agents'


urlpatterns = [
    path('',views.agents_list , name='agent_list'),

]
