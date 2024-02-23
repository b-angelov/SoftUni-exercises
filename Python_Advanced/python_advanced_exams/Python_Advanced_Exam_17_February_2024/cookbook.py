def cookbook(*args):
    recipes = list(args)
    cuisines = {x[1]:{} for x in recipes}
    [cuisines[cuisine].update({recipe:ingredients}) for recipe, cuisine, ingredients in recipes]
    cuisines = dict(sorted(cuisines.items(), key=lambda x: (-len(x[1]),x[0])))
    for cuisine,recipes in cuisines.items():
        cuisines[cuisine] = dict(sorted(recipes.items(), key= lambda x: x[0]))
    return "\n".join(
        f"{cuisine} cuisine contains {len(recipes)} recipes:\n" + \
        '\n'.join(f"  * {recipe} -> Ingredients: " + ', '.join(ingredients) for recipe,ingredients in recipes.items())
        for cuisine,recipes in cuisines.items()
    )


# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))

# print(cookbook(
#     ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
#     ))

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))

