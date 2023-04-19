# Generated by Django 4.1.5 on 2023-04-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Buy_Sell",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stock_name", models.CharField(max_length=50)),
                ("stock_price", models.IntegerField(max_length=50)),
                ("stock_shares", models.IntegerField(max_length=50)),
            ],
        ),
    ]