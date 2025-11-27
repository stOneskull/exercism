import tables

const brace = {
  '(': ')',
  '[': ']',
  '{': '}',}.toTable

proc isPaired*(line: string): bool =
  var we: seq[char]

  for you in line:
      if you in brace:
          we.add(brace[you])
      elif you in {')', ']', '}'}:
          if we.len == 0 or we.pop != you:
              return false

  return we.len == 0
