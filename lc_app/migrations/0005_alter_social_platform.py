# Generated by Django 4.1.7 on 2023-04-24 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lc_app', '0004_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='platform',
            field=models.CharField(choices=[('facebook', 'FaceBook'), ('whatsapp', 'Whats App'), ('instagram', 'Instagram'), ('twitter', 'Twitter')], default='facebook', max_length=20),
        ),
    ]
