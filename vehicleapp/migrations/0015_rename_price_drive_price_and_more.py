# Generated by Django 5.0.6 on 2024-09-05 06:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("vehicleapp", "0014_ridebook_payment_required"),
    ]

    operations = [
        migrations.RenameField(
            model_name="drive",
            old_name="price",
            new_name="Price",
        ),
        migrations.RemoveField(
            model_name="ridebook",
            name="payment_required",
        ),
        migrations.DeleteModel(
            name="Payment",
        ),
    ]
