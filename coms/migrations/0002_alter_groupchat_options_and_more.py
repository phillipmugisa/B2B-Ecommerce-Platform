# Generated by Django 4.0 on 2023-12-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupchat',
            options={},
        ),
        migrations.AlterModelOptions(
            name='interclientchat',
            options={},
        ),
        migrations.AlterModelOptions(
            name='interuserchat',
            options={},
        ),
        migrations.AlterModelOptions(
            name='orderchat',
            options={},
        ),
        migrations.AlterModelOptions(
            name='supportclientchat',
            options={},
        ),
        migrations.AlterField(
            model_name='groupchat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='interclientchat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='interuserchat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='orderchat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='supportclientchat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]