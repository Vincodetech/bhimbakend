# Generated by Django 3.1.5 on 2021-03-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_auto_20210323_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='blog/'),
        ),
    ]
