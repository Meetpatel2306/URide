# Generated by Django 5.0.1 on 2024-03-17 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0005_user_proof_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='drive',
            name='contact_number',
            field=models.CharField(default=0, max_length=30),
        ),
    ]