from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('one', views.one, name='one'),
    path('two', views.two, name='two'),
]   