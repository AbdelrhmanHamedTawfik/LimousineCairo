from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from twilio.rest import Client as twilioClient


def index(request):
    Services = Service.objects.all().order_by('-pk')[:4]
    Cars = Car.objects.all().order_by('-pk')[:4]
    Testimonials = Testimonial.objects.all().order_by('-pk')[:4]
    ContactInfos = ContactInfo.objects.get(pk=1)
    Map_obj = Map.objects.get(pk=1)
    Socials = Social.objects.all()
    context = {
        'Services': Services,
        'Cars': Cars,
        'Testimonials': Testimonials,
        'Map': Map_obj,
        'ContactInfo': ContactInfos,
        'Socials': Socials,
    }
    
    return render(request, 'index.html', context)

# def service(request, title):
#     service = Service.objects.get(title=title)
#     context = {
#         'Service': service
#     }
    
#     return render(request, 'service.html', context)

def service(request):
    
    return render(request, 'service.html')

def services(request):
    
    return render(request, 'services_comp.html')

def about(request):
    
    return render(request, 'about.html')

def fleet(request):
    Cars = Car.objects.all()
    Cars_cats = Car_category.objects.all()
    context = {
        'Categories': Cars_cats,
        'Cars': Cars
    }
    return render(request, 'fleet.html', context)

def contact(request):
    Map_obj = Map.objects.get(pk=1)
    context = {
        'Map': Map_obj,
    }
    return render(request, 'contact.html', context)

def sendWhatsapp(request):
    TWILIO_ACCOUNT_SID='AC8f79a380d2e2ea566e78ffd30729fbd3'
    TWILIO_AUTH_TOKEN='086582619f1053bffd37a6fddecc2444'
    if request.method == "POST":
        form_data = request.POST
        name = form_data['name']
        phone = form_data['phone']
        details = form_data['details']
        form_type = form_data['form_type']
        client = twilioClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        from_whatsapp_number='whatsapp:+14155238886'
        to_whatsapp_number='whatsapp:+201021759613'

        if(form_type == "1"):
            date = form_data['date']
            car = form_data['car']
            message = ''' A Client is requesting a ride:\n\n Name: ''' + name + '''\n phone: ''' + phone + '''\n date: ''' + date + '''\n car: ''' + car + '''\n details: ''' + details + '''\n '''
        else:
            message = ''' A Client is complaning or suggessting:\n\n Name: ''' + name + '''\n phone: ''' + phone + '''\n details: ''' + details + '''\n '''
        
        output = client.messages.create(body=message, from_=from_whatsapp_number, to=to_whatsapp_number)

        if(output.error_code == None):
            return JsonResponse({"success": True}, status=200)
        
        return JsonResponse({"success": False}, status=400)
    else:
        # display the form
        return JsonResponse({"success": False}, status=400)