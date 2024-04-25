# Generated by Django 4.2.3 on 2024-04-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("canteen", "0007_alter_cart_user_id_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="order_id",
            field=models.CharField(default="f", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="payment_id",
            field=models.CharField(default="f", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="signature",
            field=models.CharField(default="l", max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="menu",
            name="image",
            field=models.ImageField(
                default="default/default.jpg", upload_to="media/canteen"
            ),
        ),
    ]