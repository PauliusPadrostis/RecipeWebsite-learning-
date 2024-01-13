# Generated by Django 5.0.1 on 2024-01-13 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0009_remove_brand_grocery_store_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cuisine_tag',
            field=models.CharField(blank=True, choices=[('I', 'Italian'), ('M', 'Mexican'), ('C', 'Chinese'), ('In', 'Indian'), ('G', 'Greek'), ('T', 'Thai'), ('Med', 'Mediterranean'), ('F', 'French'), ('J', 'Japanese'), ('A', 'American'), ('ME', 'Middle Eastern')], default='', max_length=3),
        ),
    ]
