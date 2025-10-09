import strutils, algorithm

proc detectAnagrams*(word: string, candidates: openArray[string]):
  seq[string] =

  let lowerWord = word.toLowerAscii
  let sortedLowerWord = $sorted(lowerWord)

  for candidate in candidates:
    if candidate.toLowerAscii != lowerWord and
    $sorted(candidate.toLowerAscii) == sortedLowerWord:
      result.add(candidate)
