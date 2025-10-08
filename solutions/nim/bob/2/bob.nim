import strutils

proc hey*(s: string): string =
  let words = s.strip

  if words.len == 0:
    return "Fine. Be that way!"

  let isQuestion = words.endsWith("?")
  let isYelling = words.contains(Letters) and words == words.toUpper

  if isYelling and isQuestion:
    "Calm down, I know what I'm doing!"
  elif isYelling:
    "Whoa, chill out!"
  elif isQuestion:
    "Sure."
  else:
    "Whatever."