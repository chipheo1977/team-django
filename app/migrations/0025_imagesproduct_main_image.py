# Generated by Django 3.1 on 2020-09-30 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20200930_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagesproduct',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/', verbose_name='ảnh chính'),
        ),
    ]