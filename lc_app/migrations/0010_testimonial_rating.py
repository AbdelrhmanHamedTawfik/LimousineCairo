# Generated by Django 4.1.7 on 2023-05-05 20:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lc_app', '0009_service_slug_alter_contactinfo_phone_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='rating',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
