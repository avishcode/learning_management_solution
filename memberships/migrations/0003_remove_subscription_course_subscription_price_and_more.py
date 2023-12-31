# Generated by Django 4.2 on 2023-06-23 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0002_subscriptiontype_subscription_subscription_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='course',
        ),
        migrations.AddField(
            model_name='subscription',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
