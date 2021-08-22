from django.shortcuts import render


def index(request):
    return render(request, 'home.html')



def registered(request):
    return render(request, 'liberia/register.html')


def types(request):
    return render(request, 'liberia/type.html')