# Generated by Django 4.2.2 on 2023-06-26 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
        ('buyer', '0003_delete_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.clientprofile'),
        ),
    ]
