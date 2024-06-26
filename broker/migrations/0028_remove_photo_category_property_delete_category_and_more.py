# Generated by Django 5.0.6 on 2024-06-01 18:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0027_category_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='category',
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('property_name', models.CharField(max_length=100)),
                ('property_address', models.CharField(max_length=100)),
                ('first_amount', models.CharField(max_length=100)),
                ('second_amount', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('image3', models.ImageField(upload_to='')),
                ('image4', models.ImageField(upload_to='')),
                ('image5', models.ImageField(upload_to='')),
                ('image6', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
