from django.contrib import admin
from .models import *
from django.forms.models import BaseInlineFormSet


# class RecipeIngredientInline(admin.TabularInline):
#     model = RecipeIngredient
#     extra = 0
#
#
# class RecipeInstructionInline(admin.TabularInline):
#     model = RecipeInstruction
#     extra = 0
#     fields = ('step_nr', "instruction")
#
#
# class NutritionalValueInLine(admin.TabularInline):
#     model = NutriValues
#     extra = 0
#
#
# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'c_time', 'servings', 'Ingredients')
#     list_filter = ['cuisine_tag', 'dietary_tag', 'meal_type_tag', 'course_tag', 'occasion_tag', 'ingredient_based_tag',
#                    'flavor_tag', 'seasonal_tag', 'regional_tag', 'skill_tag', 'allergy_tag', 'special_tag',
#                    'prepmeth_tag', 'trend_tag']
#
#     fieldsets = (
#         ('General', {'fields': ('name', 'c_time', 'servings')}),
#         ('Tags', {'fields': (
#             'cuisine_tag', 'dietary_tag', 'meal_type_tag', 'course_tag', 'occasion_tag', 'ingredient_based_tag',
#             'flavor_tag', 'seasonal_tag', 'regional_tag', 'skill_tag', 'allergy_tag', 'special_tag',
#             'prepmeth_tag', 'trend_tag')})
#     )
#
#     search_fields = ('name',)
#     list_editable = ('c_time', 'servings')
#
#     inlines = [RecipeIngredientInline, RecipeInstructionInline]
#
#
# class IngredientAdmin(admin.ModelAdmin):
#     list_display = ('get_name', 'get_category', 'brand', 'net_weight', 'storage_type', 'get_price')
#     list_filter = ('category',)
#
#     inlines = [NutritionalValueInLine]
#
#     def get_name(self, obj):
#         return obj.name
#
#     get_name.short_description = 'Ingredient Name'
#
#     def get_category(self, obj):
#         return obj.category
#
#     get_category.short_description = 'Item category'
#
#     def get_price(self, obj):
#         return obj.price_per_unit
#
#     get_price.short_description = "Price by unit (Kg/Liter)"
#
#
# class RecipeIngredientAdmin(admin.ModelAdmin):
#     list_display = ('ingredient', 'measurement', 'amount')
#
#
# class RecipeInstructionAdmin(admin.ModelAdmin):
#     list_display = ('step_nr', 'instruction')
#
#
# # Register your models here.
# admin.site.register(NutriValues)
# admin.site.register(Category)
# admin.site.register(Ingredient, IngredientAdmin)
# admin.site.register(StorageType)
# admin.site.register(MeasurementType)
# admin.site.register(Recipe, RecipeAdmin)
# admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
# admin.site.register(RecipeInstruction, RecipeInstructionAdmin)


# Inline classes
class NutritionalValueInLine(admin.TabularInline):
    model = NutritionalValue
    extra = 0


class RecipeIngredientFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add a custom queryset for the brand field
        self.queryset = self.queryset.select_related('grocery_store_item__brand')


class RecipeIngredientsInLine(admin.TabularInline):
    model = RecipeIngredient
    formset = RecipeIngredientFormSet
    extra = 0

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        if obj:  # obj is the Recipe instance
            formset.queryset = self.model.objects.filter(recipe=obj)
        return formset


class RecipeInstructionInLine(admin.TabularInline):
    model = RecipeInstruction
    extra = 0


class BrandInLine(admin.TabularInline):
    model = Brand
    extra = 0


# Register Admin models
class GroceryStoreItemAdmin(admin.ModelAdmin):
    inlines = [NutritionalValueInLine]
    list_display = (
    'store_item_name', 'brand_name', 'net_weight', 'unit_of_measurement', 'country_of_origin', 'price_per_item',
    'price_per_uom',)

    def brand_name(self, obj):
        # Check if the brand is not None before accessing brand_name
        if obj.brand and obj.brand.brand_name:
            return obj.brand.brand_name
        return "No Brand"  # Handle the case when there's no brand


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'cooking_time', 'servings')
    inlines = [RecipeIngredientsInLine, RecipeInstructionInLine]


class NutritionalValuesAdmin(admin.ModelAdmin):
    list_display = ('grocery_store_item', 'brand_name', 'calories', 'fat', 'carbs', 'protein', 'sugar')

    def brand_name(self, obj):
        # Follow the foreign key relationship to GroceryStoreItem, and then to Brand
        if obj.grocery_store_item and obj.grocery_store_item.brand:
            return obj.grocery_store_item.brand.brand_name
        return "No Brand"  # Handle the case when there's no brand


class RecipeIngredientAdmin(admin.ModelAdmin):
    fields = ('store_item_name', 'amount', 'recipe_name')

    def store_item_name(self, obj):
        return obj.grocery_store_item.store_item_name

    def recipe_name(self, obj):
        return obj.recipe.recipe_name


# Register models
admin.site.register(NutritionalValue, NutritionalValuesAdmin)
admin.site.register(GroceryStoreItem, GroceryStoreItemAdmin)
admin.site.register(GroceryItemMeasurement)
admin.site.register(Country)
admin.site.register(IngredientMeasurement)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeInstruction)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Brand)
