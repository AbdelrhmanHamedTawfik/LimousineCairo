import datetime
import os
import shutil
from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django_resized import ResizedImageField
from .templatetags import extras

class Service_category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    title_ar = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title

class Car_category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    title_ar = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200, unique=True)
    title_ar = models.CharField(max_length=200, unique=True)
    thumbnail = ResizedImageField(quality=80, force_format='JPEG', upload_to=extras.PathRename('services', "_thumbnail"), storage=extras.OverwriteStorage())
    banner = ResizedImageField(quality=80, force_format='JPEG', upload_to=extras.PathRename('services', "_banner"), storage=extras.OverwriteStorage())
    summary = models.CharField(max_length=100)
    summary_ar = models.CharField(max_length=100)
    slider_image_1 = ResizedImageField(quality=80, force_format='JPEG', upload_to=extras.PathRename('services', "_Slider_1"), storage=extras.OverwriteStorage())
    slider_image_2 = ResizedImageField(quality=80, force_format='JPEG', upload_to=extras.PathRename('services', "_Slider_2"), storage=extras.OverwriteStorage())
    description = models.TextField()
    description_ar = models.TextField()
    description2 = models.TextField(default="random text")
    description2_ar = models.TextField(default="random text")
    category = models.ForeignKey(Service_category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("service_details", kwargs={"title": self.title})

    def save(self):
        if self.pk:
            old_record = Service.objects.get(pk=self.pk)
            if old_record:
                os.rename(os.path.join("media", 'services', old_record.title), os.path.join("media", 'services', self.title))
        super().save()

    def __str__(self):
        return self.title

class Car(models.Model):
    name = models.CharField(max_length=200)
    name_ar = models.CharField(max_length=200)
    today = datetime.date.today()
    year = today.year
    model = models.PositiveIntegerField(default=1990, validators=[MinValueValidator(1990), MaxValueValidator(int(year))])
    image = ResizedImageField(size=[500, 300], quality=80, force_format='PNG', upload_to=extras.PathRename('cars'), storage=extras.OverwriteStorage())
    person_count = models.PositiveIntegerField(default=1)
    bag_count = models.PositiveIntegerField(default=1)
    reserve_days = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Car_category, on_delete=models.CASCADE)

    def save(self):
        if self.pk:
            old_record = Car.objects.get(pk=self.pk)
            if old_record:
                os.rename(os.path.join("media", 'cars', old_record.name), os.path.join("media", 'cars', self.name))
        super().save()

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    name_ar = models.CharField(max_length=200)
    quote = models.CharField(max_length=500)
    quote_ar = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Social(models.Model):
    title = models.CharField(max_length=50)
    title_ar = models.CharField(max_length=50)
    link = models.CharField(max_length=1000)
    SOCIAL_CHOICES = (
        ('facebook','FaceBook'),
        ('whatsapp', 'Whats App'),
        ('phone','Mobile'),
        ('instagram','Instagram'),
        ('twitter','Twitter')
    )
    platform = models.CharField(max_length=20, choices=SOCIAL_CHOICES, default='facebook')

    def __str__(self):
        return self.title

class Map(models.Model):
    location_name = models.CharField(max_length=100, default='Office')
    link = models.CharField(max_length=1000)

    def __str__(self):
        return self.location_name

class ContactInfo(models.Model):
    address = models.CharField(max_length=1000)
    address_ar = models.CharField(max_length=1000)
    phone_1 = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,10}$')])
    phone_2 = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,10}$')])
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.address
    
class PagesInfo(models.Model):
    title = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200)
    description = models.TextField()
    description_ar = models.TextField()
    banner = ResizedImageField(quality=80, force_format='JPEG', upload_to=extras.PathRename('pages_banners'), storage=extras.OverwriteStorage())

    def __str__(self):
        return self.title
    
class Order(models.Model):
    name = models.CharField(max_length=400, editable=False)
    phone = models.CharField(max_length=400, editable=False)
    date = models.CharField(max_length=400, editable=False)
    details = models.CharField(max_length=400, editable=False)
    car = models.CharField(max_length=400, editable=False)
    read = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.name
    
class Complain(models.Model):
    name = models.CharField(max_length=400, editable=False)
    phone = models.CharField(max_length=400, editable=False)
    details = models.CharField(max_length=400, editable=False)
    read = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.name
    

@receiver(pre_delete, sender=Service)
def my_handler(sender, instance, **kwargs):
    shutil.rmtree(os.path.join("media", 'services', instance.title))

@receiver(pre_delete, sender=Car)
def my_handler(sender, instance, **kwargs):
    shutil.rmtree(os.path.join("media", 'cars', instance.name))