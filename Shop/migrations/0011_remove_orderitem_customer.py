# Generated by Django 3.1.5 on 2021-01-13 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0010_auto_20210113_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='customer',
        ),
    ]
