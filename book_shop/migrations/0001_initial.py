# Generated by Django 3.2.3 on 2021-05-14 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('address_replenish', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=255)),
                ('book_code', models.IntegerField()),
                ('author', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=16)),
                ('press', models.CharField(max_length=255)),
                ('press_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_code', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book_shop.book')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.IntegerField(default=-1)),
                ('menu', models.CharField(max_length=32)),
                ('menu_name', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(max_length=255)),
                ('total', models.DecimalField(decimal_places=2, max_digits=16)),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_code', models.CharField(max_length=255)),
                ('role_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=255)),
                ('user_code', models.IntegerField()),
                ('password', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shop.role')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=255)),
                ('store_code', models.IntegerField()),
                ('authorize_start_date', models.DateField()),
                ('authorize_end_date', models.DateField()),
                ('status', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shop.user')),
            ],
        ),
        migrations.CreateModel(
            name='RoleMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shop.menu')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shop.role')),
            ],
        ),
        migrations.CreateModel(
            name='OrderCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book_shop.cart')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shop.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book_shop.address')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shop.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shop.user'),
        ),
        migrations.AddField(
            model_name='cart',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book_shop.store'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shop.user'),
        ),
        migrations.AddField(
            model_name='book',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shop.store'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shop.user'),
        ),
    ]