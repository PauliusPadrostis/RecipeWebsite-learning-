# Generated by Django 5.0.1 on 2024-01-12 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0008_ingredient_brand_ingredient_net_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutrivalues',
            name='ingredient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipeapp.ingredient'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='nutritional_value',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='n_value', to='recipeapp.nutrivalues'),
        ),
    ]
