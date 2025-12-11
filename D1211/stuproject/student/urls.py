
from . import views
from django.urls import path, include

app_name = 'student'
urlpatterns = [
    path('write/', views.write, name='write'),
    path('list/', views.list, name='list'),
    path('update/<int:sno>/', views.update, name='update'),
    path('delete/<int:sno>/', views.delete, name='delete'),
    path('view/<int:sno>/', views.view, name='view'),
    
]
