# Generated by Django 3.2.4 on 2021-07-07 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amma', '0017_payed_use_statue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payed',
            old_name='use_statue',
            new_name='use_status',
        ),
    ]
