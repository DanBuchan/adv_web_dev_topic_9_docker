from django.urls import path
from . import views

urlpatterns = [
    path('simple', views.simple_view, name='simple'),
    path('', views.index, name='index'),
]
