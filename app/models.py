from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    #code = models.CharField(max_length=20, verbose_name='Mã danh mục', unique=True, null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name='Tên danh mục', unique=True)
    slug = models.CharField(max_length=200, verbose_name='Slug danh mục', unique=True, null=True, blank=True)
    status = models.BooleanField(verbose_name='Trang thái')
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Danh mục')
    code = models.CharField(max_length=10, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=200, verbose_name='Tên', unique=True)
    slug = models.CharField(max_length=200, verbose_name='Slug danh mục', unique=True,null=True, blank=True)
    image = models.ImageField(upload_to='static/images', verbose_name='Ảnh')
    image_list = models.CharField(max_length=500, verbose_name='Ảnh chi tiết', null=True, blank=True)
    price = models.FloatField(verbose_name='giá')
    discount = models.FloatField(default=None, verbose_name='giảm giá', null=True, blank=True)
    content = models.TextField(max_length=500, verbose_name='mô tả', null=True, blank=True)
    status = models.BooleanField(verbose_name='trạng thái')

    def __str__(self):
        return self.name

class Customer(models.Model):
    code = models.CharField(max_length=10, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=200, verbose_name='Tên')
    email = models.CharField(max_length=200, verbose_name='Email', unique=True)
    password = models.CharField(max_length=200, verbose_name='Mật khẩu')
    remember_token = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    code = models.CharField(max_length=10, verbose_name='Mã', unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='Mã khách hàng')
    phone = models.IntegerField(verbose_name='Số điện thoại')
    address = models.TextField(verbose_name='Địa chỉ giao hàng')
    order_note = models.TextField(verbose_name='Ghi chú đơn hàng') 
    created_order = models.DateTimeField(verbose_name='Ngày tạo đơn hàng')
    status = models.IntegerField(verbose_name='trạng thái')

    class OrderStatus:
        XacNhan = 0
        DangGiao = 1
        DaGiao = 2
        GiaoThatBai = 3
        HuyDonHang = 4

    def __str__(self):
        return self.code

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="mã đơn hàng")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="sản phẩm")
    quantity = models.IntegerField(verbose_name="số lượng")
    price = models.FloatField(verbose_name="Giá")

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="mã sản phẩm")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="mã khách hàng")
    content = models.TextField(verbose_name='nội dung')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')

    def __str__(self):
        return self.content

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name="mã bình luận")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="mã người trả lời")
    content = models.TextField(verbose_name="nội dung")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')

    def __str__(self):
        return self.content

class Event(models.Model):
    code = models.CharField(max_length=10, verbose_name='Mã sự kiện', unique=True)
    name = models.TextField(verbose_name='Tên sự kiện')
    description = models.TextField(verbose_name='mô tả sự kiện', null=True, blank=True)
    start_date = models.DateTimeField(verbose_name='ngày bắt đầu')
    end_date = models.DateTimeField(verbose_name='ngày kết thúc')

    def __str__(self):
        return self.name

class Sale(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='mã sự kiện')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='mã sản phẩm')
    discount = models.FloatField(verbose_name="khuyến mại")
    same_price = models.FloatField(verbose_name="đồng giá", null=True, blank=True)

    
    




