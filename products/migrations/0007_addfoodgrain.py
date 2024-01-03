# Generated by Django 4.2.7 on 2023-12-28 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_addbackery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addfoodgrain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('img', models.ImageField(null=True, upload_to='images')),
                ('status', models.TextField(null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'db_table': 'foodgrain_items',
            },
        ),
    ]