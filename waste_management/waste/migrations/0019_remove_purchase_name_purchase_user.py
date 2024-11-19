# Generated by Django 4.2.1 on 2023-07-18 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0018_products_stock_purchase_quantity_stock_his'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='name',
        ),
        migrations.AddField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='waste.user_registration'),
        ),
    ]
