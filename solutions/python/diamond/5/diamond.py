def rows(letter):
    if letter == 'A': return ['A']

    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    addy = alph.index(letter)
    length = addy * 2 + 1
    start = ['A'.center(length)]

    gap = -1
    lines = []

    for chap in alph[1:addy+1]:
        gap += 2
        line = chap + (' ' * gap) + chap
        lines.append(line.center(length))

    for chap in reversed(alph[1:addy]):
        gap -= 2
        line = chap + (' ' * gap) + chap
        lines.append(line.center(length))

    return start + lines + start

