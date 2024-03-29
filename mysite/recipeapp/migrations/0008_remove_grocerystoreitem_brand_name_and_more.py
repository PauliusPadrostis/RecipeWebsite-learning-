# Generated by Django 5.0.1 on 2024-01-13 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0007_brand_alter_grocerystoreitem_brand_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocerystoreitem',
            name='brand_name',
        ),
        migrations.AddField(
            model_name='brand',
            name='grocery_store_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipeapp.grocerystoreitem'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Brand name'),
        ),
    ]
