from . import views
from django.urls import path

urlpatterns = [
    path('', views.greetin, name ='greetings'),
    path('Результаты тестирований/', views.res_test, name='res_test'),

]