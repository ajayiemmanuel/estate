# Generated by Django 5.0.6 on 2024-06-02 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0042_alter_badges_bonus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='avatar.png', null=True, upload_to=''),
        ),
    ]