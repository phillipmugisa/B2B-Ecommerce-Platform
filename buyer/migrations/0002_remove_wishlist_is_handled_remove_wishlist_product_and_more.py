# Generated by Django 4.2.2 on 2023-06-26 19:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='is_handled',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='product',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='viewed_by_supplied',
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.buyer')),
            ],
        ),
    ]