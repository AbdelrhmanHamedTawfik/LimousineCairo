# Generated by Django 4.1.7 on 2023-05-05 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lc_app', '0010_testimonial_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='name_ar',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='quote_ar',
        ),
    ]
