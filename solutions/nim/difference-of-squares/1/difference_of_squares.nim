proc squareOfSum*(n: int): int =
  result = n * (n + 1) div 2
  result *= result

proc sumOfSquares*(n: int): int =
  # Faulhaber's formula for the sum of squares
  n * (n + 1) * (2 * n + 1) div 6

proc difference*(n: int): int =
  squareOfSum(n) - sumOfSquares(n)
