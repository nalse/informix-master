# Generated by Django 4.1.2 on 2023-07-06 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_hesabi', models.CharField(max_length=200)),
                ('whatsapp_hesabi', models.CharField(max_length=200)),
                ('email_hesabi', models.CharField(max_length=200)),
                ('about_photo', models.ImageField(upload_to='photos/%y/%m?%d')),
                ('about_description', models.TextField()),
                ('last_chane', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
