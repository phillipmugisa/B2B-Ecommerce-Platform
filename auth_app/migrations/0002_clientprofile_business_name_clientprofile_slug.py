# Generated by Django 4.0.6 on 2022-08-09 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="clientprofile",
            name="business_name",
            field=models.CharField(
                blank=True, max_length=256, null=True, verbose_name="Business Name"
            ),
        ),
        migrations.AddField(
            model_name="clientprofile",
            name="slug",
            field=models.SlugField(
                blank=True, null=True, unique=True, verbose_name="Safe Url"
            ),
        ),
    ]
