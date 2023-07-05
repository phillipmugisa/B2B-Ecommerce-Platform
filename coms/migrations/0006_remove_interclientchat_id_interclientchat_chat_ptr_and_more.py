# Generated by Django 4.2.2 on 2023-07-05 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coms', '0005_alter_interuserchat_participants_groupchat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interclientchat',
            name='id',
        ),
        migrations.AddField(
            model_name='interclientchat',
            name='chat_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coms.chat'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chat',
            name='chatfilepath',
            field=models.CharField(blank=True, max_length=256, null=True, unique=True, verbose_name='Chat filepath'),
        ),
    ]