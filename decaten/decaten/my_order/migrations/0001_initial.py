# Generated by Django 4.2.5 on 2024-06-27 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('payment_by_card', models.BooleanField()),
                ('number_of_card', models.IntegerField(blank=True, null=True)),
                ('month', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('cvv', models.IntegerField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]
