# Generated by Django 4.2.7 on 2023-12-13 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0002_rename_price_additems_amount_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='additems',
            table='items',
        ),
    ]
