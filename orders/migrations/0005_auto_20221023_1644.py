# Generated by Django 3.0.7 on 2022-10-23 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20221007_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.Payment', unique=True),
        ),
    ]
