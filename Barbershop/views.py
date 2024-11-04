from django.shortcuts import render

def home(request):
    return render(request, 'Barbershop/home.html')

def page1(request):
    return render(request, 'Barbershop/page1.html')

def page2(request):
    return render(request, 'Barbershop/page2.html')
