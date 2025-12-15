from . import views
from django.urls import path, include

app_name = 'board'
urlpatterns = [
    
    path('list/', views.list, name='list'),
    path('write/', views.write, name='write'),
    
    
]
