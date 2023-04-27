from lc_app.models import *


def common_data(request):
    contact_info = ContactInfo.objects.all().first()
    socials = Social.objects.all()
    pages_info = PagesInfo.objects.all()
    car_cat = Car_category.objects.all()
    orders_filtered = Order.objects.filter(read=False)
    complains_filtered = Complain.objects.filter(read=False)

    show_notifications = False

    if orders_filtered.count() > 0 or complains_filtered.count() > 0 :
        show_notifications = True

    return {
        'show_notifications': show_notifications,
        'contact_info': contact_info,
        'pages_info': pages_info,
        'socials': socials,
        'car_categories': car_cat
    }
