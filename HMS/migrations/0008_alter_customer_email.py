# Generated by Django 3.2.9 on 2021-12-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0007_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]