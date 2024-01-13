# Generated by Django 5.0.1 on 2024-01-13 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grocerystoreitem',
            old_name='brand',
            new_name='brand_name',
        ),
        migrations.RemoveField(
            model_name='grocerystoreitem',
            name='name',
        ),
        migrations.AlterField(
            model_name='grocerystoreitem',
            name='packaging',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Packaging'),
        ),
    ]
