# Generated by Django 4.1.2 on 2023-08-08 19:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_alter_question_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]