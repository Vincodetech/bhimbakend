# Generated by Django 3.1.5 on 2021-04-22 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0023_auto_20210421_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='footercms',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cms/'),
        ),
    ]