
from django.contrib import path,include
from . import views

app_name = ''
urlpatterns = [
    path('',views.index, name='index'),
]
