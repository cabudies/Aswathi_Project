# Generated by Django 3.2.4 on 2021-08-21 20:13

from django.db import migrations, models
import hod.models


class Migration(migrations.Migration):

    dependencies = [
        ('hod', '0002_headofdepartment_classes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headofdepartment',
            name='profile_pic',
            field=models.FileField(null=True, upload_to=hod.models.upload_profile),
        ),
    ]
