# Generated by Django 5.0.1 on 2024-03-15 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0004_ridebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='proof_image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]