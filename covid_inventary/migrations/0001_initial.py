# Generated by Django 3.0.7 on 2020-06-14 08:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HospDeptInventory',
            fields=[
                ('item_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('item_count', models.BigIntegerField()),
                ('item_name', models.CharField(max_length=300)),
                ('item_expiry', models.DateField()),
                ('item_desc', models.CharField(max_length=500)),
                ('item_received_date', models.DateField()),
                ('min_required', models.BigIntegerField()),
                ('item_shipping_date', models.DateField()),
                ('item_checked', models.BigIntegerField()),
                ('item_defect', models.BigIntegerField()),
                ('item_return', models.BigIntegerField()),
                ('item_return_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SellerInfo',
            fields=[
                ('s_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('seller_name', models.CharField(max_length=300)),
                ('seller_city', models.CharField(max_length=300)),
                ('seller_state', models.CharField(max_length=300)),
                ('seller_zipcode', models.CharField(max_length=10)),
                ('seller_email', models.EmailField(max_length=254)),
                ('seller_phone', models.CharField(max_length=14)),
                ('seller_lat', models.CharField(max_length=300)),
                ('seller_long', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SellerItems',
            fields=[
                ('seller_item_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('seller_item_name', models.CharField(max_length=200)),
                ('seller_item_count', models.BigIntegerField()),
                ('seller_item_expiry', models.DateField()),
                ('seller_item_category', models.CharField(max_length=200)),
                ('seller_item_request_count', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_number', models.BigIntegerField()),
                ('order_item_name', models.CharField(max_length=300)),
                ('order_item_id', models.CharField(max_length=300)),
                ('order_item_count', models.BigIntegerField()),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covid_inventary.SellerInfo')),
            ],
        ),
    ]