# Generated by Django 5.0.7 on 2024-10-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0034_alter_order_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("Accepted", "Accepted"),
                    ("Cancelled", "Cancelled"),
                    ("Completed", "Completed"),
                    ("New", "New"),
                ],
                default="New",
                max_length=10,
            ),
        ),
    ]
