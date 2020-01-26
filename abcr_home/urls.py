from django.urls import path
from . import views

app_name = 'abcr_home'

urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.show, name='show'),
    path('show_2/', views.show_2, name='show_2'),
]
