import tables, strutils

const letterScores = (proc(): Table[char, int] =

  const scoreToLetters = {
    1: "AEIOULNRST",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
  }.toTable

  for score, letters in scoreToLetters:
    for letter in letters:
      result[letter] = score
)()

proc score*(word: string): int =
  for c in word.toUpper:
    result += letterScores.getOrDefault(c)
