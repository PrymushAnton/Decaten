# Generated by Django 4.2.5 on 2024-06-16 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_product', '0006_remove_product_flavour_flavour_for_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionkey', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_product.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_product.product')),
            ],
        ),
    ]
