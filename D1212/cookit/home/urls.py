from . import views
from django.urls import path, include

app_name = ''
urlpatterns = [
    path('', views.main, name='main'),
    
]
