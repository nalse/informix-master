# Generated by Django 4.1.2 on 2023-07-31 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('topic', models.CharField(max_length=120)),
                ('sual_sayi', models.IntegerField()),
                ('time', models.IntegerField(help_text='testin ishlenilme vaxti')),
            ],
        ),
    ]
