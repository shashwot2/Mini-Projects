def cakes(recipe, available): # This code takes a recipe and the available amount of ingredients and returns the number of units that can be made from the recipe. 
    rem = []# Both should be in form of dictionaries
    for keyr,valr in recipe.items():
        keys = available.keys()
        if keyr not in keys:# Returns 0 if the there are lesser ingreidents than the amount required by the recipe
            return 0
        del keys
        for keya,vala in available.items():
            if keya in keyr:
                rem.append(vala // valr)
    return min(rem)


