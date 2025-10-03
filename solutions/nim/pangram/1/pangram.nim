import strutils

proc isPangram*(s: string): bool =
  let lower = s.toLowerAscii()
  for c in 'a'..'z':
    if c notin lower:
      return false
  return true
