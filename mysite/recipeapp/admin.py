from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(NutriValues)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(StorageType)
admin.site.register(MeasurementType)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)


