# Generated by Django 3.1 on 2020-09-24 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200924_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='mô tả'),
        ),
    ]