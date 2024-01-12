from django.contrib import admin
from .models import *


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 0


class RecipeInstructionInline(admin.TabularInline):
    model = RecipeInstruction
    extra = 0
    fields = ('step_nr', "instruction")


class NutritionalValueInLine(admin.TabularInline):
    model = NutriValues
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'c_time', 'servings', 'Ingredients')
    list_filter = ['cuisine_tag', 'dietary_tag', 'meal_type_tag', 'course_tag', 'occasion_tag', 'ingredient_based_tag',
                   'flavor_tag', 'seasonal_tag', 'regional_tag', 'skill_tag', 'allergy_tag', 'special_tag',
                   'prepmeth_tag', 'trend_tag']

    fieldsets = (
        ('General', {'fields': ('name', 'c_time', 'servings')}),
        ('Tags', {'fields': (
            'cuisine_tag', 'dietary_tag', 'meal_type_tag', 'course_tag', 'occasion_tag', 'ingredient_based_tag',
            'flavor_tag', 'seasonal_tag', 'regional_tag', 'skill_tag', 'allergy_tag', 'special_tag',
            'prepmeth_tag', 'trend_tag')})
    )

    search_fields = ('name', )
    list_editable = ('c_time', 'servings')

    inlines = [RecipeIngredientInline, RecipeInstructionInline]


class ProductAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'get_category', 'storage_type' )
    list_filter = ('category',)



    def get_name(self, obj):
        return obj.name

    get_name.short_description = 'Ingredient Name'

    def get_category(self, obj):
        return obj.category

    get_category.short_description = 'Item category'

    # def get_price(self, obj):
    #     return obj.price_per_unit
    #
    # get_price.short_description = "Price by unit (Kg/Liter)"


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('product', 'measurement', 'amount')


class RecipeInstructionAdmin(admin.ModelAdmin):
    list_display = ('step_nr', 'instruction')


class BrandIngredientsAdmin(admin.ModelAdmin):
    list_display = ('product', 'brand_name', 'net_weight', 'price_per_unit')


# Register your models here.
admin.site.register(NutriValues)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(StorageType)
admin.site.register(MeasurementType)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeInstruction)
admin.site.register(BrandIngredient, BrandIngredientsAdmin)
