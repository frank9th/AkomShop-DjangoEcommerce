# Generated by Django 3.1.5 on 2021-01-13 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0009_orderitem_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='customer',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='customer',
            field=models.ManyToManyField(to='Shop.Customer'),
        ),
    ]
