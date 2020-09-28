# Generated by Django 3.1 on 2020-09-21 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_comment_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Mã sự kiện')),
                ('name', models.TextField(verbose_name='Tên sự kiện')),
                ('start_date', models.DateTimeField(verbose_name='ngày bắt đầu')),
                ('end_date', models.DateTimeField(verbose_name='ngày kết thúc')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer', verbose_name='mã khách hàng'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='mã sản phẩm'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='remember_token',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order', verbose_name='mã đơn hàng'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='price',
            field=models.FloatField(verbose_name='Giá'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='sản phẩm'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='quantity',
            field=models.IntegerField(verbose_name='số lượng'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.comment', verbose_name='mã bình luận'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='mã người trả lời'),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.FloatField(verbose_name='khuyến mại')),
                ('same_price', models.FloatField(blank=True, null=True, verbose_name='đồng giá')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.event', verbose_name='mã sự kiện')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='mã sản phẩm')),
            ],
        ),
    ]