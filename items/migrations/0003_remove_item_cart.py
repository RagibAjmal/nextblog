# Generated by Django 4.0.2 on 2022-10-23 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_item_cart_alter_cart_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='cart',
        ),
    ]