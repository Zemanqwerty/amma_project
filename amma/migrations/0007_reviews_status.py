# Generated by Django 3.2.4 on 2021-06-26 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amma', '0006_auto_20210624_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='status',
            field=models.CharField(default='Новый', max_length=11),
        ),
    ]
