from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'app1/home.html')


def list(request):
    context = {
       'Manufactures': Manufacture.objects.all()
    }
    return render(request, 'app1/list.html', context=context)

def detail(request, id):
    Manufactury = get_object_or_404(Manufacture, pk=id)
    context = {
        'Manufactury': Manufactury
    }
    return render(request, 'app1/detail.html', context=context)

