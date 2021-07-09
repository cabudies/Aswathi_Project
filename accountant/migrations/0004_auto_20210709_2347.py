# Generated by Django 3.0.7 on 2021-07-09 18:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0003_auto_20210708_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(blank=True, default='pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='payment',
            name='txn_id',
            field=models.CharField(blank=True, default=uuid.UUID('24bc2310-38c8-4512-a133-417ed9792b6d'), max_length=100),
        ),
    ]
