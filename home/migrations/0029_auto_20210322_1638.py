# Generated by Django 3.1.5 on 2021-03-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20210312_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='educattion/'),
        ),
        migrations.AddField(
            model_name='educationcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='educattion/'),
        ),
        migrations.AddField(
            model_name='educationsubcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='educattion/'),
        ),
        migrations.AddField(
            model_name='edusubjects',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='educattion/'),
        ),
    ]