class Luhn:
    def __init__(self, card_num):
        self.num = card_num.replace(' ','')[::-1]

    def valid(self):
        if len(self.num) < 2 or any(
            not digit.isdigit() for digit in self.num):
            return False

        digits = []

        for position, digit in enumerate(self.num):
            digit = int(digit)
            if position % 2:
                digit *= 2
                if digit > 9:
                    digit -= 9
            digits.append(digit)

        return sum(digits) % 10 == 0
