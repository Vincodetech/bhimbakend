# Generated by Django 3.1.5 on 2021-01-22 06:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0004_auto_20210122_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privecyandprolicy',
            name='descriptions',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
