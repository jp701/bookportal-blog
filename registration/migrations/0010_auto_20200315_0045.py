# Generated by Django 3.0.2 on 2020-03-14 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_auto_20200315_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldbooks',
            name='buyer_name',
            field=models.CharField(max_length=30),
        ),
    ]
