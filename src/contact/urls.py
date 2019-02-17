from django.urls import path
from . import views


app_name = 'contact'


urlpatterns = [
    path('' , views.send_mail , name='send_mail'),
    path('success/' , views.success , name='success'),
]
