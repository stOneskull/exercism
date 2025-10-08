type
  Allergen* = enum
    Eggs, Peanuts, Shellfish, Strawberries, Tomatoes, Chocolate, Pollen, Cats

proc isAllergicTo*(score: int, allergen: Allergen): bool =
  bool(score and 1 shl ord(allergen))

proc allergies*(score: int): set[Allergen] =
  for allergen in Allergen:
    if isAllergicTo(score, allergen):
      result.incl(allergen)
