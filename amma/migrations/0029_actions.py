# Generated by Django 3.2.4 on 2021-07-18 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amma', '0028_auto_20210709_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id_action', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('action_img', models.ImageField(upload_to='images/')),
                ('action_name', models.CharField(max_length=50)),
            ],
        ),
    ]
