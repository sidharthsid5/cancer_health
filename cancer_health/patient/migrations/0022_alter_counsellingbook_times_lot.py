# Generated by Django 5.1.4 on 2025-05-24 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0021_remove_regfreevig_coupon_counsellingbook_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counsellingbook',
            name='Times_lot',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
