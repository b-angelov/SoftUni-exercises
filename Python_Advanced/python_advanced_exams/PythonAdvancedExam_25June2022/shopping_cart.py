def shopping_cart(*products):
    meals = {"Soup":set(),"Pizza":set(),"Dessert":set()}
    limits = {"Soup":3,"Pizza":4,"Dessert":2}
    for prod in products:
        if prod == "Stop":
            break
        meal,product = prod
        if len(meals[meal]) < limits[meal]:
            meals[meal].add(prod)
    meals = {meal:sorted(list(meals[meal])) for meal in meals}
    meals = sorted(meals.items(), key=lambda x: (-len(x[1]),x[0]))
    if all(not products for meal,products in meals):
        return "No products in the cart!"
    return "\n".join(f"{meal}:" + ("\n" + "\n".join(f" - {product[1]}" for product in products) if products else "") for meal,products in meals)