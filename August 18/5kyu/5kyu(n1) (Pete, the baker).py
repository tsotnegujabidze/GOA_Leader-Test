def cakes(recipe, available):
    max = float('inf')
    for ingredient, amount in recipe.items():
        if ingredient in available:
            max = min(max, available[ingredient] // amount)
        else:
            return 0
    return max