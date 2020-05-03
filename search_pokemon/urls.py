from django.urls import path
from . import views

urlpatterns = [
    path('', views.about),
    path('<str:name>/', views.info_pokemon)
]