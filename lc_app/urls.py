from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/<str:title>', views.service, name='service'),
    # path('service', views.service, name='service'),
    path('services', views.services, name='services'),
    path('about-us', views.about, name='about-us'),
    path('contact-us', views.contact, name='contact-us'),
    path('fleet', views.fleet, name='fleet'),
    path('request', views.request, name='request'),
    path('order-complain', views.order_complain, name='order-complain'),
    path('update-order', views.update_order, name='update-order'),
    path('update-complain', views.update_complain, name='update-complain')
]