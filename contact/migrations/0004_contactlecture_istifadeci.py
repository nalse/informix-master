# Generated by Django 4.1.2 on 2023-08-27 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0003_rename_contact_lecture_contactlecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactlecture',
            name='istifadeci',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
