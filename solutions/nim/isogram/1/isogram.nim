import tables
import strutils

proc isIsogram*(s: string): bool =
  var counts = initCountTable[char]()
  for c in s.toLower:
    if c.isAlphaAscii:
      counts.inc(c)
      if counts[c] > 1:
        return false
  true
