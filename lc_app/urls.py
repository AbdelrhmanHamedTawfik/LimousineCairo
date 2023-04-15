from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    # path('services/<str:title>/', views.service, name='service'),
    path('service', views.service, name='service'),
    path('services', views.services, name='services'),
    path('about-us', views.about, name='about-us'),
    path('contact-us', views.contact, name='contact-us'),
    path('fleet', views.fleet, name='fleet'),
    path('sendWhatsapp/', views.sendWhatsapp, name='sendWhatsapp'),
]