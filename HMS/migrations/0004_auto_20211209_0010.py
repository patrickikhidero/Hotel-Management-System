# Generated by Django 3.2.9 on 2021-12-09 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0003_remove_booking_payment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='numbers',
        ),
        migrations.AddField(
            model_name='room',
            name='room_number',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
