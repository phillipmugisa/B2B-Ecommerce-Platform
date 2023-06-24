# Generated by Django 4.2.2 on 2023-06-24 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_product_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcolor',
            name='name_ar',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='productcolor',
            name='name_de',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='productcolor',
            name='name_en',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='productcolor',
            name='name_fr',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='productmaterial',
            name='name_ar',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='productmaterial',
            name='name_de',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='productmaterial',
            name='name_en',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='productmaterial',
            name='name_fr',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
    ]