# Generated by Django 4.1.5 on 2023-04-15 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0004_alter_buy_sell_stock_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="buy_sell",
            name="stock_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="buy_sell", name="stock_price", field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="buy_sell", name="stock_shares", field=models.BigIntegerField(),
        ),
    ]