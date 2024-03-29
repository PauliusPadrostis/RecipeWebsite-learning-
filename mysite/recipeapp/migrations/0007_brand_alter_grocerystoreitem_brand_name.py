# Generated by Django 5.0.1 on 2024-01-13 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0006_remove_recipeingredient_ingredient_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipeapp.grocerystoreitem')),
            ],
        ),
        migrations.AlterField(
            model_name='grocerystoreitem',
            name='brand_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipeapp.brand'),
        ),
    ]
