# Generated by Django 3.2.4 on 2021-07-07 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amma', '0016_auto_20210706_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='payed',
            name='use_statue',
            field=models.CharField(default='не использован', max_length=50),
        ),
    ]
