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
    if unit == 9:
        return code[9][pwr]
    if unit >= 5:
        return code[5][pwr] + code[1][pwr] * (unit - 5)
    if unit == 4:
        return code[4][pwr]
    return code[1][pwr] * unit


def roman(number):
    out = ''

    for level in reversed(range(4)):
        out += roman_loop(number, level)
        number %= 10**level

    return out
