# Generated by Django 3.2.4 on 2021-08-21 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20210804_0143'),
        ('hod', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headofdepartment',
            name='classes',
            field=models.ManyToManyField(to='course.MyClass'),
        ),
    ]