# Generated by Django 4.2 on 2023-06-23 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0003_remove_subscription_course_subscription_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='price',
        ),
        migrations.AddField(
            model_name='subscriptiontype',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
    ]
