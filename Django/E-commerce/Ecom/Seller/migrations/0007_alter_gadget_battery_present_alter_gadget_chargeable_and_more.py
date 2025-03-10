# Generated by Django 5.0.6 on 2024-07-09 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0006_delete_seller_alter_clothes_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gadget',
            name='battery_present',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='gadget',
            name='chargeable',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='gadget',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='gadget',
            name='price',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='gadget',
            name='product_img',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='gadget',
            name='weight',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='price',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='product_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='product_img',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='weight',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='price',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='product_img',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='weight',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='toy',
            name='age',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='toy',
            name='chargeable',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='toy',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='toy',
            name='price',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='toy',
            name='product_img',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='toy',
            name='weight',
            field=models.CharField(max_length=10),
        ),
    ]
