# Generated by Django 4.0.6 on 2022-07-31 07:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_app', '0001_initial'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_complete', models.BooleanField(default=False, verbose_name='Contract completed')),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='auth_app.buyer')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_service', to='supplier.service')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier', to='auth_app.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiry_date', models.DateField(blank=True, null=True, verbose_name='Plan expiry data')),
                ('duration', models.CharField(choices=[('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Annually', 'Annually')], max_length=256, verbose_name='Duration')),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
            ],
        ),
        migrations.CreateModel(
            name='MembershipPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=3, max_digits=12, verbose_name='Price')),
                ('currency', models.CharField(max_length=6, verbose_name='Currency')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Safe Url')),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
            ],
        ),
        migrations.CreateModel(
            name='ModeOfPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('transaction_count', models.IntegerField(default=0, verbose_name='Number of transactions')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Safe Url')),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
            ],
        ),
        migrations.CreateModel(
            name='MembershipReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256, verbose_name='Address')),
                ('payment_id', models.CharField(max_length=256, verbose_name='Payment Id')),
                ('amount_paid', models.DecimalField(decimal_places=3, max_digits=12, verbose_name='Total Amount Paid')),
                ('currency', models.CharField(max_length=6, verbose_name='Currency')),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.membership')),
                ('model_of_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.modeofpayment')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.membershipplan'),
        ),
        migrations.AddField(
            model_name='membership',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.supplier'),
        ),
        migrations.CreateModel(
            name='ContractReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256, verbose_name='Address')),
                ('payment_id', models.CharField(max_length=256, verbose_name='Payment Id')),
                ('amount_paid', models.DecimalField(decimal_places=3, max_digits=12, verbose_name='Total Amount Paid')),
                ('currency', models.CharField(max_length=6, verbose_name='Currency')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.contract')),
                ('model_of_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.modeofpayment')),
            ],
        ),
    ]
