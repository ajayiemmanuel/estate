# Generated by Django 5.0.6 on 2024-06-02 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0046_addfund_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='payout1',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
