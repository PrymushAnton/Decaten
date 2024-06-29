# Generated by Django 4.2.5 on 2024-06-27 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog_product', '0008_productincart_flavour'),
        ('user', '0003_alter_myuser_number'),
        ('my_order', '0002_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('flavour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog_product.flavour')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.myuser')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='orders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_order.orders'),
        ),
    ]