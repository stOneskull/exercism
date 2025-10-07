proc binarySearch*(a: openArray[int], val: int): int =
  var
    left = 0
    right = a.high

  while left <= right:
    let mid = (left + right) div 2
    let guess = a[mid]

    if guess == val:
      return mid
    elif guess > val:
      right = mid - 1
    else: # guess < val
      left = mid + 1

  return -1
