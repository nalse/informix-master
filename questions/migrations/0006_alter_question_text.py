# Generated by Django 4.1.2 on 2023-08-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_alter_question_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(),
        ),
    ]