# Generated by Django 3.0.2 on 2020-03-14 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_auto_20200315_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldbooks',
            name='buyer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.User'),
        ),
        migrations.AlterField(
            model_name='soldbooks',
            name='seller_name',
            field=models.CharField(max_length=30),
        ),
    ]
