# Generated by Django 5.0.6 on 2024-06-01 16:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0025_alter_payout1_charge_alter_payout2_charge_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('main_balance', models.CharField(default='30', max_length=200, null=True)),
                ('intrest_balance', models.CharField(default='0', max_length=200, null=True)),
                ('total_deposit', models.CharField(default='0', max_length=200, null=True)),
                ('total_payout', models.CharField(default='0', max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]