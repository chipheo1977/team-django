# Generated by Django 3.1 on 2020-09-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200921_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='mô tả sự kiện'),
        ),
    ]