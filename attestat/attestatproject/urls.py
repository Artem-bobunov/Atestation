from django.urls import path
from . import views
from django.urls import path
from .views import *

urlpatterns = [
    #path('', views.listObjects, name ='greetings'),
    path('Список вопросов/', views.listObjects, name ='list'),
    path('Результат/', views.results, name ='results'),


]