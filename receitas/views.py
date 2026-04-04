from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def ViewHome(request):
#     return HttpResponse("HOME")

def ViewHome(request):
    return render(request, 'receitas/Home.html')

def ViewContato(request):
    return HttpResponse("Contato")

def ViewSobre(request):
    return HttpResponse("Sobre")