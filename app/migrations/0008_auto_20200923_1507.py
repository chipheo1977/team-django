# Generated by Django 3.1 on 2020-09-23 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Mã danh mục'),
        ),
    ]