from django.urls import path

from .views import InicioView

urlpatterns = [
    path('',InicioView),
]