# Generated by Django 4.1.2 on 2023-07-08 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_soyad', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('haqqinda', models.TextField()),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('tarix', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
