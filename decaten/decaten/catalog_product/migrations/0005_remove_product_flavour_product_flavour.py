# Generated by Django 4.2.5 on 2024-06-13 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_product', '0004_remove_flavour_product_product_flavour_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='flavour',
        ),
        migrations.AddField(
            model_name='product',
            name='flavour',
            field=models.ManyToManyField(blank=True, null=True, to='catalog_product.flavour'),
        ),
    ]
