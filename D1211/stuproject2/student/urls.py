from . import views
from django.urls import path, include

app_name = 'student'
urlpatterns = [
    path('write/', views.write, name='write'),
    path('list/', views.list, name='list'),
    
]
