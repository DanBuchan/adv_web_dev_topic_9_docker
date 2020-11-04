from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gene/<int:pk>', views.gene, name='gene'),
    path('list/<str:type>', views.list, name='list'),
    path('poslist/', views.poslist, name='poslist'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
