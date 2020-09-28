# Generated by Django 3.1.1 on 2020-09-16 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=200, verbose_name='Tên')),
                ('email', models.CharField(max_length=200, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=200, verbose_name='Mật khẩu')),
                ('remember_token', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Mã')),
                ('phone', models.IntegerField(verbose_name='Số điện thoại')),
                ('address', models.TextField(verbose_name='Địa chỉ giao hàng')),
                ('order_note', models.TextField(verbose_name='Ghi chú đơn hàng')),
                ('created_order', models.DateTimeField(verbose_name='Ngày tạo đơn hàng')),
                ('status', models.IntegerField(verbose_name='trạng thái')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.customer', verbose_name='Mã khách hàng')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=200, null=True, unique=True, verbose_name='Slug danh mục'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.IntegerField(default=1, verbose_name='Trang thái'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(default=1, verbose_name='trạng thái'),
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]
