# Generated by Django 3.1.5 on 2021-02-03 10:18

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news/')),
                ('youtube_link', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateField(default=datetime.datetime.now)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
