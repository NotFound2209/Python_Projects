# Generated by Django 4.2.3 on 2023-09-24 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='img',
            field=models.ImageField(upload_to='timmy_photo'),
        ),
    ]
