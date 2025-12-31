with open('input', 'r') as f:
    lines = [line.rstrip('\n') for line in f if line.rstrip('\n') != '']

fresh_ids = [l for l in lines if "-" in l]
ingredient_ids = [l for l in lines if "-" not in l]

#print(fresh_ids)
#print(ingredient_ids)

fresh_ingredients = set()
for ingredient_id in ingredient_ids:
    print(ingredient_id)
    for fresh_id in fresh_ids:
        start, end = fresh_id.split("-")
        if int(ingredient_id) >= int(start) and int(ingredient_id) <= int(end):
            fresh_ingredients.add(int(ingredient_id))
            break
print(len(fresh_ingredients))
