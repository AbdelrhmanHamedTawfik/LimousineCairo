from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/<str:slug>', views.service, name='service'),
    path('services', views.services, name='services'),
    path('about-us', views.about, name='about-us'),
    path('contact-us', views.contact, name='contact-us'),
    path('fleet', views.fleet, name='fleet'),
    path('request', views.request, name='request'),
    path('order-complain', views.order_complain, name='order-complain'),
    path('update-order', views.update_order, name='update-order'),
    path('update-complain', views.update_complain, name='update-complain'),
    path('delete-order', views.delete_order, name='delete-order'),
    path('delete-complain', views.delete_complain, name='delete-complain'),
    path('insert-review', views.insert_review, name='insert-review'),
]