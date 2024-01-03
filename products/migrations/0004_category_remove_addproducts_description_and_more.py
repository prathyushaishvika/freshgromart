# Generated by Django 4.2.7 on 2023-12-19 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_addproducts_image_addproducts_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.TextField(max_length=50, null=True)),
                ('c_image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='addproducts',
            name='description',
        ),
        migrations.AddField(
            model_name='addproducts',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
    ]
