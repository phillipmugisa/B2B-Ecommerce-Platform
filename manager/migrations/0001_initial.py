# Generated by Django 4.0.6 on 2022-07-31 07:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import manager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Country or City')),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Safe Url')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Safe Url')),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
            ],
        ),
        migrations.CreateModel(
            name='Showroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('image', models.ImageField(upload_to=manager.models.get_file_path, verbose_name='Image')),
                ('visits', models.IntegerField(default=0, verbose_name='Number of visits')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Safe Url')),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.location')),
                ('store', models.ManyToManyField(default=None, related_name='store', to='supplier.store')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=manager.models.get_file_path, verbose_name='Service Image')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Safe Url')),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.service')),
            ],
        ),
    ]
