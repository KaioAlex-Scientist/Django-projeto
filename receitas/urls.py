from django.urls import path
from receitas.views import ViewHome, ViewContato, ViewSobre
urlpatterns = [
    path('', ViewHome),
    path('sobre/', ViewSobre),
    path('contato/', ViewContato),
]