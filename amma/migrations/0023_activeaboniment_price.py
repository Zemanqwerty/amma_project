# Generated by Django 3.2.4 on 2021-07-09 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amma', '0022_aboniment_activeaboniment'),
    ]

    operations = [
        migrations.AddField(
            model_name='activeaboniment',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
