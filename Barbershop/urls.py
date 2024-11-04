from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='barbershop_home'),
    path('page1/', views.page1, name='barbershop_page1'),
    path('page2/', views.page2, name='barbershop_page2'),
]
