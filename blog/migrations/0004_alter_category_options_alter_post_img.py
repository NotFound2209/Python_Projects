# Generated by Django 4.2.3 on 2023-10-05 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='blog', verbose_name='Image'),
        ),
    ]
