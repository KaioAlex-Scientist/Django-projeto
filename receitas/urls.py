from django.urls import path
from receitas.views import ViewHome

urlpatterns = [
    path('', ViewHome),
]