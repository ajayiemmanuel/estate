# Generated by Django 5.0.6 on 2024-06-02 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0052_alter_addfund_options_alter_payout1_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addfund',
            options={'verbose_name': 'Addfund', 'verbose_name_plural': 'Addfunds'},
        ),
        migrations.AlterModelOptions(
            name='investment',
            options={'verbose_name': 'Investment', 'verbose_name_plural': 'Investments'},
        ),
        migrations.AlterModelOptions(
            name='payout1',
            options={'verbose_name': 'Payout1', 'verbose_name_plural': 'Payout1s'},
        ),
        migrations.AlterModelOptions(
            name='payout2',
            options={'verbose_name': 'Payout2', 'verbose_name_plural': 'Payout2s'},
        ),
        migrations.AlterModelOptions(
            name='payout3',
            options={'verbose_name': 'Payout3', 'verbose_name_plural': 'Payout3s'},
        ),
        migrations.AlterModelOptions(
            name='withdraw',
            options={'verbose_name': 'Withdraw', 'verbose_name_plural': 'Withdraws'},
        ),
    ]