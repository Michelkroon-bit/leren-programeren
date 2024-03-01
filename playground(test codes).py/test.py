pizzas = [
    {"name": "Margherita", "diameter": 30},
    {"name": "Pepperoni", "diameter": 35},
    {"name": "Hawaiian", "diameter": 40},
    {"name": "Vegetarian", "diameter": 32},
    {"name": "Quattro Stagioni", "diameter": 38},
    {"name": "Capricciosa", "diameter": 36},
    {"name": "BBQ Chicken", "diameter": 34},
    {"name": "Seafood", "diameter": 37},
    {"name": "Meat Lover's", "diameter": 42},
    {"name": "Mushroom", "diameter": 33}
]

gesoorteerde_lijst = sorted(pizzas , key = lambda x:x["diameter"], reverse= True) 
for x in gesoorteerde_lijst:
    print(f"{x['name']}, {x['diameter']}cm")
    