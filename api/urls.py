from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name='Routes'),
    path('lists/', views.getToDoList, name='getToDoList'),

]