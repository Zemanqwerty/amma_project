# Generated by Django 3.2.4 on 2021-06-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amma', '0008_auto_20210626_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='id',
        ),
        migrations.AddField(
            model_name='application',
            name='id_application',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
