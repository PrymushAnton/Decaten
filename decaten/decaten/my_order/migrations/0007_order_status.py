# Generated by Django 4.2.5 on 2024-06-28 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_order', '0006_remove_order_date_order_day_num_order_month_num_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
