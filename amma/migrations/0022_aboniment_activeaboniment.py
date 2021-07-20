# Generated by Django 3.2.4 on 2021-07-09 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amma', '0021_auto_20210708_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboniment',
            fields=[
                ('id_aboniment', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('aboniment_category', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('aboniment_number', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='ActiveAboniment',
            fields=[
                ('id_aboniment', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('aboniment_name', models.CharField(max_length=256)),
                ('aboniment_image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
            ],
        ),
    ]
