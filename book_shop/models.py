from django.db import models


# Create your models here.


class Role(models.Model):
    role_code = models.CharField(
        max_length=255
    )
    role_name = models.CharField(
        max_length=32
    )

    def __str__(self):
        return self.role_name + ':' + self.role_code

    def test(self):
        return self.role_code == 'admin'


class User(models.Model):
    real_name = models.CharField(
        max_length=32
    )
    username = models.CharField(
        max_length=255
    )
    user_code = models.IntegerField(

    )
    password = models.CharField(
        max_length=255
    )
    phone = models.IntegerField(

    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE
    )
    create_date = models.DateTimeField(

    )


class Store(models.Model):
    store_name = models.CharField(
        max_length=255
    )
    store_code = models.IntegerField(

    )
    authorize_start_date = models.DateField(

    )
    authorize_end_date = models.DateField(

    )
    status = models.BooleanField(

    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


class Book(models.Model):
    book_name = models.CharField(
        max_length=255
    )
    book_code = models.IntegerField(

    )
    author = models.CharField(
        max_length=255
    )
    price = models.DecimalField(
        max_digits=16,
        decimal_places=2
    )
    press = models.CharField(
        max_length=255
    )
    press_date = models.DateField(

    )
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE
    )


class Cart(models.Model):
    cart_code = models.CharField(
        max_length=255
    )
    store = models.ForeignKey(
        Store,
        on_delete=models.DO_NOTHING
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.DO_NOTHING
    )
    amount = models.IntegerField(

    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


class Order(models.Model):
    order_code = models.CharField(
        max_length=255
    )
    total = models.DecimalField(
        max_digits=16,
        decimal_places=2
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    create_date = models.DateTimeField(

    )
    update_date = models.DateTimeField(

    )


class Menu(models.Model):
    parent_id = models.IntegerField(
        default=-1
    )
    menu = models.CharField(
        max_length=32
    )
    menu_name = models.CharField(
        max_length=255
    )
    path = models.CharField(
        max_length=255
    )


class Address(models.Model):
    country = models.CharField(
        max_length=100
    )
    province = models.CharField(
        max_length=100
    )
    city = models.CharField(
        max_length=100
    )
    district = models.CharField(
        max_length=100
    )
    address_replenish = models.CharField(
        max_length=255
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


class OrderAddress(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.DO_NOTHING
    )


class RoleMenu(models.Model):
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE
    )


class OrderCart(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.DO_NOTHING
    )
