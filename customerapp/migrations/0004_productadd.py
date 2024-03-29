# Generated by Django 4.2.7 on 2023-12-13 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0003_delete_pro'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('description', models.TextField(null=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
