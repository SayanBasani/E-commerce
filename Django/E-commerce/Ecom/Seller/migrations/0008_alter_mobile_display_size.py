# Generated by Django 5.0.6 on 2024-07-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0007_alter_gadget_battery_present_alter_gadget_chargeable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='display_size',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
