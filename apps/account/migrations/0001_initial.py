# Generated by Django 4.2.2 on 2023-06-25 20:35

import apps.account.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('bairro', models.CharField(max_length=150, verbose_name='Bairro')),
                ('endereco', models.CharField(max_length=150, verbose_name='Endereço')),
                ('cidade', models.CharField(max_length=150, verbose_name='Cidade')),
                ('numero', models.IntegerField(max_length=5, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters', max_length=15, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Enter a valid username.', 'invalid')], verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_trusty', models.BooleanField(default=False, help_text='Designates whether this user has confirmed his account.', verbose_name='trusty')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('occupation', models.CharField(blank=True, max_length=150, null=True, verbose_name='Ocupação')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, verbose_name='CPF')),
                ('phone', models.CharField(blank=True, max_length=13, null=True, verbose_name='Telefone')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=apps.account.models.upload_to_user_photos, verbose_name='Avatar')),
                ('addresses', models.ManyToManyField(blank=True, to='account.endereco', verbose_name='Endereços')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
