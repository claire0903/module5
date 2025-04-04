# Generated by Django 5.1.5 on 2025-03-24 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaterBottle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('brand', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.CharField(max_length=20)),
                ('mouth_size', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('current_quantity', models.PositiveIntegerField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyInventoryApp.supplier')),
            ],
        ),
    ]
