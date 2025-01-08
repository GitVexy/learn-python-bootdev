## My brain was too broken for this one, so I grabbed the solution. This is close to what I was trying to do anyway

def check_ingredient_match(recipe, ingredients):
    correct = 0
    incorrect_ingredients = []

    for i in range(len(recipe)):
        if recipe[i] == ingredients[i]:
            correct += 1
        else:
            incorrect_ingredients.append(recipe[i])

    percentage = correct / len(recipe) * 100
    return percentage, incorrect_ingredients
