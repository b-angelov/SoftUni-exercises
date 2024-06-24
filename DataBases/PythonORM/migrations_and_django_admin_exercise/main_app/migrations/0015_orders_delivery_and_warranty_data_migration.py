# Generated by Django 5.0.4 on 2024-06-22 19:11
from datetime import timedelta

from django.db import migrations

def set_delivery(apps, schema_editor):
    Order = apps.get_model("main_app","Order")

    all_orders = Order.objects.all()

    for order in all_orders:
        if order.status == "P":
            order.delivery = order.order_date + timedelta(days=3)
            order.save()
        if order.status == "C":
            order.warranty = "24 months"
            order.save()
        if order.status == "CN":
            order.delete()

def reset_delivery(apps, schema_editor):
    for order in apps.get_model("main_app", "Order").objects.all():
        order.delivery = order.order_date - timedelta(days=3)
        order.warranty = "No warranty"

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_order'),
    ]

    operations = [
        migrations.RunPython(set_delivery, reverse_code=reset_delivery)

    ]