# Generated by Django 5.0.6 on 2024-05-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=1, max_length=14),
        ),
    ]
