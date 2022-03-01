pets = [
    {
    "animal":"Iguana",
    "name":"Iggy",
    "food":"Veggies",
    "mealsPerDay":1
   },
   {
    "animal":"Goldfish",
    "name":"Goldy",
    "food":"Flakes",
    "mealsPerDay":3
   }
]

for pet in pets:
    print(pet["animal"], "-", pet["name"])
