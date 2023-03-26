from recipes.models import IngredientRecipe
from django.db.models import Sum


def get_shopping_list(ingredients):
    shopping_list = 'Купить в магазине:'
    for ingredient in ingredients:
        shopping_list += (
            f"\n{ingredient['ingredient__name']} "
            f"({ingredient['ingredient__measurement_unit']}) - "
            f"{ingredient['amount']}")
    return shopping_list


def get_ingredients_shopping_card(request):
    ingredients = IngredientRecipe.objects.filter(
        recipe__shopping_list__user=request.user
    ).order_by('ingredient__name').values(
        'ingredient__name', 'ingredient__measurement_unit'
    ).annotate(amount=Sum('amount'))
    return ingredients
