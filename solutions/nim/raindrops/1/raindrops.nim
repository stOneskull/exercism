proc convert*(n: int): string =
  if n mod 3 == 0:
    result.add "Pling"
  if n mod 5 == 0:
    result.add "Plang"
  if n mod 7 == 0:
    result.add "Plong"
  if result.len == 0:
    result = $n
