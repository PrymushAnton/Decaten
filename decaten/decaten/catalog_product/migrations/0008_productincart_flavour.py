# Generated by Django 4.2.5 on 2024-06-16 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_product', '0007_cart_productincart'),
    ]

    operations = [
        migrations.AddField(
            model_name='productincart',
            name='flavour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog_product.flavour'),
        ),
    ]
