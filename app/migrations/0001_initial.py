# Generated by Django 3.1.1 on 2020-09-16 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='Mã danh mục')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Tên danh mục')),
                ('slug', models.CharField(default=None, max_length=200, unique=True, verbose_name='Slug danh mục')),
                ('status', models.IntegerField(default=1, max_length=10, verbose_name='Trang thái')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Tên')),
                ('slug', models.CharField(default=None, max_length=200, unique=True, verbose_name='Slug danh mục')),
                ('image', models.CharField(max_length=300, verbose_name='Ảnh')),
                ('image_list', models.CharField(max_length=500, verbose_name='Ảnh chi tiết')),
                ('price', models.FloatField(verbose_name='giá')),
                ('discount', models.FloatField(default=None, verbose_name='giảm giá')),
                ('content', models.CharField(max_length=500, verbose_name='mô tả')),
                ('status', models.IntegerField(default=1, max_length=10, verbose_name='trạng thái')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.category', verbose_name='Danh mục')),
            ],
        ),
    ]
