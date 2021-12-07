# Generated by Django 3.2.9 on 2021-12-07 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0018_auto_20211207_0542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='price',
        ),
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]