# Generated by Django 5.1.4 on 2025-05-15 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0013_alter_guidelines_guides'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scancenter',
            name='District',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.dist'),
        ),
        migrations.AlterField(
            model_name='scancenter',
            name='Mobile',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='scancenter',
            name='Phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
