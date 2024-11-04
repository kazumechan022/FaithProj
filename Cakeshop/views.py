from django.shortcuts import render

def about(request):
    return render(request, 'Cakeshop/about.html')

def one(request):
    return render(request, 'Cakeshop/one.html')

def two(request):
    return render(request, 'Cakeshop/two.html')
