# Generated by Django 4.1.2 on 2023-08-14 21:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0003_quiz_qiymet'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='tarix',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]