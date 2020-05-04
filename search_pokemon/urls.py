from django.urls import path
from . import views

urlpatterns = [
    path('', views.about),
    path('name/<str:name>/', views.info_pokemon)
]