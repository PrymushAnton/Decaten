# Generated by Django 4.2.5 on 2024-06-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_order', '0008_order_cvv_order_month_order_number_of_card_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
