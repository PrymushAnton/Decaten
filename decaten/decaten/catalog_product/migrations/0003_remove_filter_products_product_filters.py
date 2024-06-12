# Generated by Django 4.2.5 on 2024-06-12 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_product', '0002_filter_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filter',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='filters',
            field=models.ManyToManyField(blank=True, null=True, to='catalog_product.filter'),
        ),
    ]
