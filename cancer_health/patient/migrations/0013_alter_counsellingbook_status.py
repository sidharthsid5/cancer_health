# Generated by Django 5.1.4 on 2025-05-23 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0012_alter_counsellingbook_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counsellingbook',
            name='Status',
            field=models.CharField(default='New', max_length=10, null=True),
        ),
    ]
