import tables, strutils

proc countWords*(s: string): Table[string, int] =
  var cleanString = ""

  for letter in s.toLowerAscii:
    if letter.isAlphaNumeric or letter == '\'':
      cleanString.add(letter)
    else:
      cleanString.add(' ')

  for word in cleanString.split(' '):
    let cleanWord = word.strip(chars = {'\''})
    if cleanWord.len > 0:
      result.mgetOrPut(cleanWord, 0) += 1
