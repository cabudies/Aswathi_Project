# Generated by Django 3.0.7 on 2021-07-28 19:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0004_auto_20210709_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(blank=True, default='success', max_length=10),
        ),
        migrations.AlterField(
            model_name='payment',
            name='txn_id',
            field=models.CharField(blank=True, default=uuid.UUID('3b0d08ca-25cb-487d-8daf-ea17d80cf1fc'), max_length=100),
        ),
    ]