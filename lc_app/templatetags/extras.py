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


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(name))
        return name

@deconstructible
class PathRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(str(uuid4().hex)[:4], ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)