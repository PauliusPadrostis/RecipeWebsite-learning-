from django.db import models


# Create your models here.
class StorageType(models.Model):
    name = models.CharField(verbose_name="Storage type", max_length=100)

    class Meta:
        verbose_name = 'Storage type'
        verbose_name_plural = 'Storage types'

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(verbose_name="Category", max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.name}"


class NutriValues(models.Model):
    ing_name = models.CharField(verbose_name="Name", max_length=100, default="None")
    cal_per_100 = models.FloatField(verbose_name="Calories per 100 g/ml")
    fat = models.FloatField(verbose_name="Fat")
    sat_fat = models.FloatField(verbose_name="Saturated Fat")
    carbs = models.FloatField(verbose_name="Carbs")
    sugar = models.FloatField(verbose_name="Sugar")
    protein = models.FloatField(verbose_name="Protein")
    salt = models.FloatField(verbose_name="Salt")

    class Meta:
        verbose_name = 'Nutrient value'
        verbose_name_plural = 'Nutrient values'

    def __str__(self):
        return f"{self.ing_name}"


class Ingredient(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    nutritional_value = models.ForeignKey("NutriValues", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    storage_type = models.ForeignKey("StorageType", on_delete=models.SET_NULL, null=True)
    price_per_unit = models.FloatField(verbose_name="Price")

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

    def __str__(self):
        return f"{self.name}"


class MeasurementType(models.Model):
    name = models.CharField(verbose_name="Measurement", max_length=100)

    class Meta:
        verbose_name = 'Measurement type'
        verbose_name_plural = 'Measurement types'

    def __str__(self):
        return f"{self.name}"


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey("Ingredient", on_delete=models.SET_NULL, null=True)
    measurement = models.ForeignKey("MeasurementType", on_delete=models.SET_NULL, null=True)
    amount = models.FloatField(verbose_name="Amount")
    recipe = models.ForeignKey("Recipe", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Recipe ingredient'
        verbose_name_plural = 'Recipe ingredients'

    def __str__(self):
        return f"{self.ingredient}, {self.amount} {self.measurement}"


class Recipe(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    c_time = models.IntegerField(verbose_name="Cooking time")
    servings = models.IntegerField(verbose_name="Servings")

    def display_ingredients(self):
        return ', '.join(str(ingredient.ingredient.name) for ingredient in self.recipeingredient_set.all())


    CUISINE_TAGS = (
        ("I", "Italian"), ("M", "Mexican"), ("C", "Chinese"), ("In", "Indian"), ("G", "Greek"),
        ("T", "Thai"), ("Med", "Mediterranean"), ("F", "French"), ("J", "Japanese"), ("A", "American")
    )

    DIETARY_TAGS = (
        ("V", "Vegetarian"), ("VG", "Vegan"), ("GF", "Gluten-Free"), ("DF", "Dairy-Free"),
        ("NF", "Nut-Free"), ("LC", "Low-Carb"), ("K", "Keto"), ("P", "Paleo")
    )

    MEAL_TYPE_TAGS = (
        ("B", "Breakfast"), ("L", "Lunch"), ("D", "Dinner"), ("S", "Snack"),
        ("DE", "Dessert"), ("A", "Appetizer"), ("SD", "Side Dish"), ("MC", "Main Course"), ("SL", "Salad")
    )

    COURSE_TAGS = (
        ("S", "Soup"), ("SD", "Salad"), ("P", "Pasta"), ("R", "Rice"), ("C", "Curry"),
        ("SF", "Stir-Fry"), ("G", "Grilled"), ("RO", "Roasted"), ("B", "Baked"), ("SC", "Slow Cooker"),
    )

    OCCASION_TAGS = (
        ("H", "Holiday"), ("P", "Party"), ("PI", "Picnic"), ("PL", "Potluck"),
        ("QE", "Quick & Easy"), ("WN", "Weeknight"), ("DN", "Date Night"),
    )

    INGREDIENT_BASED_TAGS = (
        ("CH", "Chicken"), ("B", "Beef"), ("SEA", "Seafood"), ("V", "Vegetables"),
        ("TO", "Tofu"), ("Q", "Quinoa"), ("AV", "Avocado"), ("SP", "Sweet Potato"),
    )

    FLAVOR_TAGS = (
        ("SP", "Spicy"), ("SW", "Sweet"), ("SAV", "Savory"), ("T", "Tangy"), ("CR", "Creamy"),
        ("GA", "Garlicky"), ("CI", "Citrusy"), ("HE", "Herby"),
    )

    SEASONAL_TAGS = (
        ("SU", "Summer"), ("FA", "Fall"), ("WI", "Winter"), ("SP", "Spring"),
    )

    REGIONAL_TAGS = (
        ("SO", "Southern"), ("NO", "Northern"), ("CO", "Coastal"), ("MO", "Mountain"), ("TR", "Tropical"),
        ("DE", "Desert"),
    )

    SKILL_LEVEL_TAGS = (
        ("BF", "Beginner-Friendly"), ("I", "Intermediate"), ("A", "Advanced"), ("QE", "Quick & Simple"),
    )

    ALLERGY_FRIENDLY_TAGS = (
        ("NF", "Nut-Free"), ("GF", "Gluten-Free"), ("DF", "Dairy-Free"), ("EF", "Egg-Free"), ("SF", "Soy-Free"),
    )

    SPECIAL_DIET_TAGS = (
        ("K", "Keto"), ("P", "Paleo"), ("W30", "Whole30"), ("LC", "Low-Calorie"), ("HP", "High-Protein"),
        ("LF", "Low-Fat"),
    )

    PREPARATION_METHOD_TAGS = (
        ("G", "Grilled"), ("RO", "Roasted"), ("B", "Baked"), ("ST", "Steamed"), ("SC", "Slow Cooker"),
        ("IP", "Instant Pot"),
    )

    CULINARY_TREND_TAGS = (
        ("PB", "Plant-Based"), ("SF", "Superfood"), ("FU", "Fusion"), ("GO", "Gourmet"), ("SI", "Street Food-Inspired"),
    )

    cuisine_tag = models.CharField(max_length=3, choices=CUISINE_TAGS, blank=True, default="")
    dietary_tag = models.CharField(max_length=3, choices=DIETARY_TAGS, blank=True, default="")
    meal_type_tag = models.CharField(max_length=3, choices=MEAL_TYPE_TAGS, blank=True, default="")
    course_tag = models.CharField(max_length=3, choices=COURSE_TAGS, blank=True, default="")
    occasion_tag = models.CharField(max_length=3, choices=OCCASION_TAGS, blank=True, default="")
    ingredient_based_tag = models.CharField(max_length=3, choices=INGREDIENT_BASED_TAGS, blank=True, default="")
    flavor_tag = models.CharField(max_length=3, choices=FLAVOR_TAGS, blank=True, default="")
    seasonal_tag = models.CharField(max_length=3, choices=SEASONAL_TAGS, blank=True, default="")
    regional_tag = models.CharField(max_length=3, choices=REGIONAL_TAGS, blank=True, default="")
    skill_tag = models.CharField(max_length=3, choices=SKILL_LEVEL_TAGS, blank=True, default="")
    allergy_tag = models.CharField(max_length=3, choices=ALLERGY_FRIENDLY_TAGS, blank=True, default="")
    special_tag = models.CharField(max_length=3, choices=SPECIAL_DIET_TAGS, blank=True, default="")
    prepmeth_tag = models.CharField(max_length=3, choices=PREPARATION_METHOD_TAGS, blank=True, default="")
    trend_tag = models.CharField(max_length=3, choices=CULINARY_TREND_TAGS, blank=True, default="")

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return f"{self.name}"


class RecipeInstruction(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.SET_NULL, null=True)
    instruction = models.TextField(verbose_name="Instructions", max_length=1000)
    step_nr = models.IntegerField(verbose_name="Step Nr:")

    class Meta:
        verbose_name = 'Recipe instruction'
        verbose_name_plural = 'Recipe instructions'
