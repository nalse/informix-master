# Generated by Django 4.1.2 on 2023-08-10 15:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0020_alter_question_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='img',
        ),
        migrations.AddField(
            model_name='question',
            name='sual',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
