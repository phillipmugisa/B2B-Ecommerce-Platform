# Generated by Django 4.0 on 2023-12-12 09:19

import auth_app.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('first_name_ar', models.CharField(blank=True, max_length=150, null=True, verbose_name='first name')),
                ('first_name_fr', models.CharField(blank=True, max_length=150, null=True, verbose_name='first name')),
                ('first_name_de', models.CharField(blank=True, max_length=150, null=True, verbose_name='first name')),
                ('first_name_en', models.CharField(blank=True, max_length=150, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('last_name_ar', models.CharField(blank=True, max_length=150, null=True, verbose_name='last name')),
                ('last_name_fr', models.CharField(blank=True, max_length=150, null=True, verbose_name='last name')),
                ('last_name_de', models.CharField(blank=True, max_length=150, null=True, verbose_name='last name')),
                ('last_name_en', models.CharField(blank=True, max_length=150, null=True, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('account_type', models.CharField(choices=[('ADMIN', 'Admin'), ('SUPPORT', 'Support'), ('SUPPLIER', 'Supplier'), ('BUYER', 'Buyer')], max_length=50, verbose_name='Account Type')),
                ('image', models.ImageField(blank=True, default='assets/imgs/resources/profiledefault.png', null=True, upload_to=auth_app.models.get_file_path, verbose_name='Image')),
                ('is_email_activated', models.BooleanField(default=False, verbose_name='Email Activated')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SupportProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responses', models.IntegerField(default=0, verbose_name='Responses to clients')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=256, verbose_name='Business Name')),
                ('business_name_ar', models.CharField(max_length=256, null=True, verbose_name='Business Name')),
                ('business_name_fr', models.CharField(max_length=256, null=True, verbose_name='Business Name')),
                ('business_name_de', models.CharField(max_length=256, null=True, verbose_name='Business Name')),
                ('business_name_en', models.CharField(max_length=256, null=True, verbose_name='Business Name')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Safe Url')),
                ('business_description', models.TextField(verbose_name='Business Description')),
                ('business_description_ar', models.TextField(null=True, verbose_name='Business Description')),
                ('business_description_fr', models.TextField(null=True, verbose_name='Business Description')),
                ('business_description_de', models.TextField(null=True, verbose_name='Business Description')),
                ('business_description_en', models.TextField(null=True, verbose_name='Business Description')),
                ('country', models.CharField(max_length=256, verbose_name='Country')),
                ('country_ar', models.CharField(max_length=256, null=True, verbose_name='Country')),
                ('country_fr', models.CharField(max_length=256, null=True, verbose_name='Country')),
                ('country_de', models.CharField(max_length=256, null=True, verbose_name='Country')),
                ('country_en', models.CharField(max_length=256, null=True, verbose_name='Country')),
                ('country_code', models.CharField(max_length=20, verbose_name='Country Code')),
                ('country_code_ar', models.CharField(max_length=20, null=True, verbose_name='Country Code')),
                ('country_code_fr', models.CharField(max_length=20, null=True, verbose_name='Country Code')),
                ('country_code_de', models.CharField(max_length=20, null=True, verbose_name='Country Code')),
                ('country_code_en', models.CharField(max_length=20, null=True, verbose_name='Country Code')),
                ('city', models.CharField(max_length=256, verbose_name='City')),
                ('city_ar', models.CharField(max_length=256, null=True, verbose_name='City')),
                ('city_fr', models.CharField(max_length=256, null=True, verbose_name='City')),
                ('city_de', models.CharField(max_length=256, null=True, verbose_name='City')),
                ('city_en', models.CharField(max_length=256, null=True, verbose_name='City')),
                ('mobile_user', models.CharField(max_length=20, verbose_name='Number')),
                ('mobile_user_ar', models.CharField(max_length=20, null=True, verbose_name='Number')),
                ('mobile_user_fr', models.CharField(max_length=20, null=True, verbose_name='Number')),
                ('mobile_user_de', models.CharField(max_length=20, null=True, verbose_name='Number')),
                ('mobile_user_en', models.CharField(max_length=20, null=True, verbose_name='Number')),
                ('vat_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='VAT Number')),
                ('legal_etity_identifier', models.CharField(blank=True, max_length=256, null=True, verbose_name='Legal Entity Identifier')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('customer_id', models.CharField(blank=True, max_length=30, null=True, verbose_name='Braintree customer id')),
                ('image', models.FileField(default='test/django.png', upload_to=auth_app.models.get_file_path, verbose_name='Business Image')),
                ('team', models.ManyToManyField(blank=True, related_name='team_members', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth_app.user',),
            managers=[
                ('buyer', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth_app.user',),
            managers=[
                ('supplier', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth_app.user',),
            managers=[
                ('support', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
