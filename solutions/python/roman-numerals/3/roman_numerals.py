code = {
    9: ['IX', 'XC', 'CM'],
    5: ['V', 'L', 'D'],
    4: ['IV', 'XL', 'CD'],
    1: ['I', 'X', 'C'],
    }


def roman_loop(num, pwr):
    unit = num // 10**pwr
    if pwr == 3:
        return 'M' * unit
    if unit in (4, 9):
        return code[unit][pwr]
    if unit >= 5:
        return code[5][pwr] + code[1][pwr] * (unit-5)
    return code[1][pwr] * unit


def roman(number):
    out = ''

    for pwr in (3, 2, 1, 0):
        out += roman_loop(number, pwr)
        number %= 10**pwr

    return out
