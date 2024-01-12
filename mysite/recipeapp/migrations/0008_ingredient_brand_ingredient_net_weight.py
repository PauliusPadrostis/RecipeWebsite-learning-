# Generated by Django 5.0.1 on 2024-01-12 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0007_alter_recipeinstruction_instruction'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='brand',
            field=models.CharField(max_length=100, null=True, verbose_name='Brand'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='net_weight',
            field=models.FloatField(null=True, verbose_name='Net weight (g/ml)'),
        ),
    ]