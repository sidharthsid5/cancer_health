# Generated by Django 5.1.4 on 2025-05-15 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0019_alter_dietarytip_diet_tips'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietarysupply',
            name='daily_serving',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dietarysupply',
            name='food_group',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
