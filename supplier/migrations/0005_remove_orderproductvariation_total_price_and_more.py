# Generated by Django 4.2.2 on 2023-06-26 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0004_remove_order_products_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproductvariation',
            name='total_price',
        ),
        migrations.AddField(
            model_name='orderproductvariation',
            name='max_total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Max Total Price'),
        ),
        migrations.AddField(
            model_name='orderproductvariation',
            name='min_total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Min Total Price'),
        ),
    ]
