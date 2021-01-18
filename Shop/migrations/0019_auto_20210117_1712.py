# Generated by Django 3.1.5 on 2021-01-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0018_auto_20210114_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placedorder',
            name='status',
            field=models.BooleanField(blank=True, choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Out for delivery', 'Out for delivery')], max_length=200, null=True),
        ),
    ]
