# Generated by Django 4.2.3 on 2023-10-16 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_details_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_details',
            name='product_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Product Price'),
        ),
    ]
