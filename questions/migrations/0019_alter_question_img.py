# Generated by Django 4.1.2 on 2023-08-10 08:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0018_remove_answer_solution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='img',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
