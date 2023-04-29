import datetime
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import *

class ServiceSitemap(Sitemap):
	changefreq = "daily"
	priority = 1
	
	def items(self):
		return Service.objects.all()
	
	def lastmod(self, obj):
		return datetime.date.today()
	
	def location(self,obj):
		return '/services/%s' % (obj.slug)
	
class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return ['index', 'services', 'about-us', 'fleet', 'contact-us', 'request']

    def location(self, item):
        return reverse(item)