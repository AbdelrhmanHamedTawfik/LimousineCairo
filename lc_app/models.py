import datetime
from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator 
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
    thumbnail = models.ImageField(upload_to=extras.PathRename('services'), storage=extras.OverwriteStorage())
    summary = models.CharField(max_length=100)
    summary_ar = models.CharField(max_length=100)
    slider_image_1 = models.ImageField(upload_to=extras.PathRename('services'), storage=extras.OverwriteStorage())
    slider_image_2 = models.ImageField(upload_to=extras.PathRename('services'), storage=extras.OverwriteStorage())
    description = models.TextField()
    description_ar = models.TextField()
    category = models.ForeignKey(Service_category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Car(models.Model):
    name = models.CharField(max_length=200)
    name_ar = models.CharField(max_length=200)
    today = datetime.date.today()
    year = today.year
    model = models.PositiveIntegerField(default=1990, validators=[MinValueValidator(1990), MaxValueValidator(int(year))])
    image = models.ImageField(upload_to=extras.PathRename('cars'), storage=extras.OverwriteStorage())
    person_count = models.PositiveIntegerField(default=1)
    bag_count = models.PositiveIntegerField(default=1)
    reserve_days = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Car_category, on_delete=models.CASCADE)

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
    location_name = models.CharField(max_length=100, default='Home')
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
    