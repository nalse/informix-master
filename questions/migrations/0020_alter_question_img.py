# Generated by Django 4.1.2 on 2023-08-10 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0019_alter_question_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]