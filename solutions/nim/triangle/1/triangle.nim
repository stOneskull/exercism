import algorithm

proc isValid(sides: array[3, int]): bool =
  let sortedSides = sorted(sides)
  sortedSides[0] > 0 and sortedSides[0] + sortedSides[1] >= sortedSides[2]

proc isEquilateral*(sides: array[3, int]): bool =
  isValid(sides) and sides[0] == sides[1] and sides[1] == sides[2]

proc isIsosceles*(sides: array[3, int]): bool =
  isValid(sides) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])

proc isScalene*(sides: array[3, int]): bool =
  isValid(sides) and sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]
