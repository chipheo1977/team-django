# Generated by Django 3.1 on 2020-09-20 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200916_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Slug danh mục'),
        ),
    ]
