import std/sets

proc sum*(limit: int, factors: openArray[int]): int =
  var multiples: HashSet[int]

  for factor in factors:
    if factor == 0: continue
    var current = factor
    while current < limit:
      multiples.incl(current)
      current += factor

  for multiple in multiples:
    result += multiple
