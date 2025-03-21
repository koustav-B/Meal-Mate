# Generated by Django 4.2.4 on 2024-06-24 04:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0026_alter_order_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("Accepted", "Accepted"),
                    ("New", "New"),
                    ("Cancelled", "Cancelled"),
                    ("Completed", "Completed"),
                ],
                default="New",
                max_length=10,
            ),
        ),
    ]
