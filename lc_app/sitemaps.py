from django.contrib.sitemaps import Sitemap

from .models import *

class ServiceSitemap(Sitemap):
		changefreq = "weekly"
		priority = 0.9
		
		def items(self):
				return Service.objects.all()
		
		def lastmod(self, obj):
				return obj.updated
		changefreq = "weekly"
		priority = 0.9
		
		def items(self):
				return Complain.objects.all()
		
		def lastmod(self, obj):
				return obj.updated