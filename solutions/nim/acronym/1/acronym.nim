import strutils

proc abbreviate*(s: string): string =
  var prevIsBoundary = true
  for c in s:
    if c.isAlphaAscii and prevIsBoundary:
      result.add(c.toUpperAscii)
    prevIsBoundary = not (c.isAlphaAscii or c == '\'')
