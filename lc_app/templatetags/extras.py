import os
from django import template
from ..models import *
from django.core.files.storage import FileSystemStorage
from django.utils.deconstruct import deconstructible
from uuid import uuid4

register = template.Library()

def get_decimal(value, counter):
    round_value = round(value * 2) / 2
    return counter - round_value

def get_by_index(indexable, i):
    return indexable[i]

def get_social_link(indexable, title):
    return indexable.filter(title=title).values().first()['link']

register.filter('get_decimal', get_decimal)
register.filter('get_by_index', get_by_index)
register.filter('get_social_link', get_social_link)

def defineSlug(slug, slug_ar):
    new_slug = slug.replace(" ", "-")
    new_slug_ar = slug_ar.replace(" ", "-")

    return new_slug + "#" + new_slug_ar


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join("media", name))
        return name

@deconstructible
class PathRename(object):

    def __init__(self, sub_path, fixed_name=""):
        self.path = sub_path
        self.fixed_name = fixed_name

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance:
            filename = '{}.{}'.format(str(instance) + self.fixed_name, ext)
            return os.path.join(self.path, str(instance), filename)
        else:
            # set filename as random string
            filename = '{}.{}'.format(str(uuid4().hex)[:4], ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)