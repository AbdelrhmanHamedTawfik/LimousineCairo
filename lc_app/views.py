from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *


def index(request):
    Services = Service.objects.all().order_by('-pk')[:4]
    Cars = Car.objects.all().order_by('-pk')[:4]
    Testimonials = Testimonial.objects.all().order_by('-pk')[:4]
    ContactInfos = ContactInfo.objects.get(pk=1)
    Map_obj = Map.objects.get(pk=1)
    Socials = Social.objects.all()
    Orders = Order.objects.filter(read=False)
    Complains = Complain.objects.filter(read=False)
    show_notifications = False

    if Orders.count() > 0 or Complains.count() > 0 :
        show_notifications = True

    context = {
        'Services': Services,
        'Cars': Cars,
        'Testimonials': Testimonials,
        'Map': Map_obj,
        'ContactInfo': ContactInfos,
        'Socials': Socials,
        'show_notifications': show_notifications,
    }
    
    return render(request, 'index.html', context)

def service(request, title):
    service = Service.objects.get(title=str(title))
    category = Service_category.objects.get(pk=service.category.pk)
    Orders = Order.objects.filter(read=False)
    Complains = Complain.objects.filter(read=False)
    show_notifications = False

    if Orders.count() > 0 or Complains.count() > 0 :
        show_notifications = True

    context = {
        'Service': service,
        'Category': category,
        'show_notifications': show_notifications,
    }
    
    return render(request, 'service.html', context)

# def service(request):

#     return render(request, 'service.html')

def services(request):
    Services_cats = Service_category.objects.all()
    Orders = Order.objects.filter(read=False)
    Complains = Complain.objects.filter(read=False)
    show_notifications = False

    if Orders.count() > 0 or Complains.count() > 0 :
        show_notifications = True

    context = {
        'Categories': Services_cats,
        'show_notifications': show_notifications,
    }

    return render(request, 'services_comp.html', context)

def about(request):
    Orders = Order.objects.filter(read=False)
    Complains = Complain.objects.filter(read=False)
    show_notifications = False

    if Orders.count() > 0 or Complains.count() > 0 :
        show_notifications = True

    context = {
        'show_notifications': show_notifications,
    }

    return render(request, 'about.html', context)

def fleet(request):
    Cars_cats = Car_category.objects.all()
    Orders = Order.objects.filter(read=False)
    Complains = Complain.objects.filter(read=False)
    show_notifications = False

    if Orders.count() > 0 or Complains.count() > 0 :
        show_notifications = True

    context = {
        'Categories': Cars_cats,
        'show_notifications': show_notifications,
    }

    return render(request, 'fleet.html', context)

def contact(request):
    Map_obj = Map.objects.get(pk=1)
    Orders = Order.objects.filter(read=False)
    Complains = Complain.objects.filter(read=False)
    show_notifications = False

    if Orders.count() > 0 or Complains.count() > 0 :
        show_notifications = True

    context = {
        'Map': Map_obj,
        'show_notifications': show_notifications,
    }

    return render(request, 'contact.html', context)

def request(request):
    Orders = Order.objects.all()
    Complains = Complain.objects.all()

    Orders_Filtered = Order.objects.filter(read=False)
    Complains_Filtered = Complain.objects.filter(read=False)

    show_notifications = False

    if Orders_Filtered.count() > 0 or Complains_Filtered.count() > 0 :
        show_notifications = True

    context = {
        'Orders': Orders,
        'Complains': Complains,
        'show_notifications': show_notifications,
    }

    return render(request, 'request.html', context)

def order_complain(request):
    if request.method == "POST":
        form_data = request.POST
        name = form_data['name']
        phone = form_data['phone']
        details = form_data['details']
        form_type = form_data['form_type']

        if(form_type == "1"):
            date = form_data['date']
            car = form_data['car']
            Order.objects.create(
               name = name,
               phone = phone,
               date = date,
               details = details,
               car = car
           )
        else:
            Complain.objects.create(
               name = name,
               phone = phone,
               details = details
           )
        
        return JsonResponse({"success": True}, status=200)
        
    return JsonResponse({"success": False}, status=400)


def update_order(request):
    order = Order.objects.get(pk=request.POST['id'])
    order.read = True
    order.save()

    Orders_Filtered = Order.objects.filter(read=False)
    Complains_Filtered = Complain.objects.filter(read=False)

    show_notifications = False

    if Orders_Filtered.count() > 0 or Complains_Filtered.count() > 0 :
        show_notifications = True


    return JsonResponse({"success": True, "show_notifications":show_notifications}, status=200)

def update_complain(request):
    complain = Complain.objects.get(pk=request.POST['id'])
    complain.read = True
    complain.save()

    Orders_Filtered = Order.objects.filter(read=False)
    Complains_Filtered = Complain.objects.filter(read=False)

    show_notifications = False

    if Orders_Filtered.count() > 0 or Complains_Filtered.count() > 0 :
        show_notifications = True

    return JsonResponse({"success": True, "show_notifications":show_notifications}, status=200)