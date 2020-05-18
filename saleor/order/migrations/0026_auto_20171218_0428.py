# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-18 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("order", "0025_auto_20171214_1015")]

    operations = [
        migrations.AlterModelOptions(name="orderline", options={}),
        migrations.RemoveField(model_name="deliverygroup", name="shipping_price"),
        migrations.AddField(
            model_name="order",
            name="shipping_price",
            field=models.DecimalField(
                decimal_places=4,
                default=0,
                editable=False,
                max_digits=12,
                verbose_name="shipping price",
            ),
        ),
        migrations.AlterField(
            model_name="orderhistoryentry",
            name="status",
            field=models.CharField(
                choices=[("open", "Open"), ("closed", "Closed")],
                max_length=32,
                verbose_name="order status",
            ),
        ),
    ]
