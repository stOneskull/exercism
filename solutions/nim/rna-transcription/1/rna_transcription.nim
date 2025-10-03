proc toRna*(dna: string): string =
  for c in dna:
    case c
    of 'G': result.add 'C'
    of 'C': result.add 'G'
    of 'T': result.add 'A'
    of 'A': result.add 'U'
    else:
      raise newException(ValueError, "Invalid nucleotide: " & $c)
