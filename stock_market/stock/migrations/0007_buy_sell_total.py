# Generated by Django 4.1.5 on 2023-04-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0006_rename_stock_shares_buy_sell_number_of_shares_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="buy_sell",
            name="total",
            field=models.FloatField(blank=True, null=True),
        ),
    ]