# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.ADD,name='add'),
    path ('edit',views.EDIT, name = 'edit'),
]
