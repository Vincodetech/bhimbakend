# Generated by Django 3.1.5 on 2021-03-22 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20210322_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationcategory',
            name='photo',
            field=models.ImageField(blank=True, default='', null=True, upload_to='educattion/'),
        ),
    ]