# Generated by Django 5.0.6 on 2024-05-30 15:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0012_alter_withdraw_unique_together_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='withdraw',
            order_with_respect_to='user',
        ),
        migrations.AlterUniqueTogether(
            name='withdraw',
            unique_together={('user',)},
        ),
    ]
