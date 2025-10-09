import strutils, unicode

proc containsLetters(s: string): bool =
  for r in s.runes:
    if r.isAlpha:
      return true
  return false

proc hey*(s: string): string =
  let words = s.strip

  if words.len == 0:
    return "Fine. Be that way!"

  let isQuestion = words.endsWith("?")
  let isYelling = words == words.toUpper and words.containsLetters

  if isYelling and isQuestion:
    "Calm down, I know what I'm doing!"
  elif isYelling:
    "Whoa, chill out!"
  elif isQuestion:
    "Sure."
  else:
    "Whatever."