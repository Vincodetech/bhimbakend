# Generated by Django 3.1.5 on 2021-01-20 14:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_name', models.CharField(default='', max_length=150)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateField(default=datetime.datetime.now)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(default='', max_length=150)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateField(default=datetime.datetime.now)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(default='', max_length=150)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateField(default=datetime.datetime.now)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_name', models.CharField(default='', max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateField(default=datetime.datetime.now)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village_name', models.CharField(default='', max_length=150)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateField(default=datetime.datetime.now)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.block')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(default='', max_length=150)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateField(default=datetime.datetime.now)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.country')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intrests', models.CharField(choices=[('News', 'News'), ('Sports', 'Sports'), ('Entertainment', 'Entertainment'), ('Politics', 'Politics'), ('Business', 'Business'), ('Education', 'Education')], default='', max_length=255)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users/')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='', max_length=15)),
                ('street1', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('street2', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('add_block', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Add Taluka')),
                ('add_village', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Add Village')),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('add_international', models.TextField(blank=True, null=True, verbose_name='International Address')),
                ('profession_type', models.CharField(blank=True, choices=[('Student', 'Student'), ('Profession', 'Profession'), ('Business', 'Business'), ('Goverment Servent', 'Goverment Servent'), ('Social Worker', 'Social Worker'), ('Private Job', 'Private Job')], default='', max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Profession Details')),
                ('created_at', models.DateField(default=datetime.datetime.now)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('add_city', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='home.city', verbose_name='Add District')),
                ('add_state', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='home.state')),
                ('country', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='home.country')),
                ('degree', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='home.degree', verbose_name='Select Education Degree')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.state'),
        ),
        migrations.AddField(
            model_name='block',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.city'),
        ),
    ]
