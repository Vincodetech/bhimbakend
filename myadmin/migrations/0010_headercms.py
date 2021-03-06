# Generated by Django 3.1.5 on 2021-01-27 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0009_aboutuscms_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderCms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cms/')),
                ('facebook', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('google', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('instagram', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateField(default=datetime.datetime.now)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
