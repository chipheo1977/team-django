# Generated by Django 3.1 on 2020-10-03 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_remove_imagesproduct_main_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_list',
        ),
    ]