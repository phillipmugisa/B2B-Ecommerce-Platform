# Generated by Django 4.0.6 on 2022-09-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_alter_chatroom_chatfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='chatfile',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Chat file'),
        ),
    ]