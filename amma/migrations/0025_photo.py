# Generated by Django 3.2.4 on 2021-07-09 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amma', '0024_rename_aboniment_image_activeaboniment_certificate_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id_photo', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
