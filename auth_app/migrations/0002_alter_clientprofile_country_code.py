# Generated by Django 4.0.6 on 2022-08-18 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientprofile",
            name="country_code",
            field=models.CharField(max_length=5, verbose_name="Country Code"),
        ),
    ]