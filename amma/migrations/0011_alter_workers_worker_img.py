# Generated by Django 3.2.4 on 2021-06-29 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amma', '0010_workers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='worker_img',
            field=models.ImageField(upload_to='media'),
        ),
    ]