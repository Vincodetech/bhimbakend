# Generated by Django 3.1.5 on 2021-01-27 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0007_auto_20210127_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuscms',
            name='mission_title',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
