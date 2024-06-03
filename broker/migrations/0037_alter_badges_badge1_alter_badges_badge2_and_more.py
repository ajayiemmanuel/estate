# Generated by Django 5.0.6 on 2024-06-02 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0036_badges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badges',
            name='badge1',
            field=models.CharField(choices=[('locked', 'locked'), ('open', 'open')], default='locked', max_length=24),
        ),
        migrations.AlterField(
            model_name='badges',
            name='badge2',
            field=models.CharField(choices=[('locked', 'locked'), ('open', 'open')], default='locked', max_length=24),
        ),
        migrations.AlterField(
            model_name='badges',
            name='badge3',
            field=models.CharField(choices=[('locked', 'locked'), ('open', 'open')], default='locked', max_length=24),
        ),
        migrations.AlterField(
            model_name='badges',
            name='badge4',
            field=models.CharField(choices=[('locked', 'locked'), ('open', 'open')], default='locked', max_length=24),
        ),
    ]