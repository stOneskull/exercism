import tables

const brace = {
  '(': ')',
  '[': ']',
  '{': '}',}.toTable

proc isPaired*(line: string): bool =
  var stack: seq[char]

  for you in line:
      if you in brace:
          stack.add(brace[you])
      elif you in {')', ']', '}'}:
          if stack.len == 0 or stack.pop != you:
              return false

  return stack.len == 0