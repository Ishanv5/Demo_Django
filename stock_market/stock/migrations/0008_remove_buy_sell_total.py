# Generated by Django 4.1.5 on 2023-04-19 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0007_buy_sell_total"),
    ]

    operations = [
        migrations.RemoveField(model_name="buy_sell", name="total",),
    ]