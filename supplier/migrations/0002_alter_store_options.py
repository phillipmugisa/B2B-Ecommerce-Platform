# Generated by Django 4.1.7 on 2023-03-05 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='store',
            options={'ordering': ['-id']},
        ),
    ]
