import algorithm, sets

proc isValid(sides: array[3, int]): bool =
  let sortedSides = sorted(sides)
  sortedSides[0] > 0 and sortedSides[0] + sortedSides[1] >= sortedSides[2]

proc isEquilateral*(sides: array[3, int]): bool =
  isValid(sides) and toHashSet(sides).len == 1

proc isIsosceles*(sides: array[3, int]): bool =
  # An equilateral triangle is also isosceles, so we check for 1 or 2 unique sides.
  isValid(sides) and toHashSet(sides).len <= 2

proc isScalene*(sides: array[3, int]): bool =
  isValid(sides) and toHashSet(sides).len == 3
