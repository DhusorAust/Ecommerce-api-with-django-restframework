# Generated by Django 4.0 on 2022-01-25 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_addtocart_is_ordered'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
