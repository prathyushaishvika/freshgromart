# Generated by Django 4.2.7 on 2023-12-04 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_column='name', null=True)),
                ('number', models.PositiveIntegerField(db_column='number', null=True)),
                ('email', models.TextField(db_column='email', null=True)),
                ('password', models.TextField(db_column='password', null=True)),
            ],
            options={
                'db_table': 'customer_signin',
            },
        ),
    ]
