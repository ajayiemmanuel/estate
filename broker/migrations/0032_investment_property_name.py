# Generated by Django 5.0.6 on 2024-06-02 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0031_remove_investment_property_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='property_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]