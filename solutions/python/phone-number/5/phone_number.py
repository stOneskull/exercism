import re

class PhoneNumber:
    def __init__(self, phone_number):
        # Check for invalid characters first.
        if re.search(r"[a-zA-Z]", phone_number):
            raise ValueError("letters not permitted")
        if re.search(r"[@:!]", phone_number):
            raise ValueError("punctuations not permitted")

        number = "".join(filter(str.isdigit, phone_number))

        if len(number) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(number) == 11:
            if not number.startswith("1"):
                raise ValueError("11 digits must start with 1")
            number = number[1:]
        if len(number) != 10:
            raise ValueError("must not be fewer than 10 digits")
        if number.startswith("0"):
            raise ValueError("area code cannot start with zero")
        if number.startswith("1"):
            raise ValueError("area code cannot start with one")
        if number[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if number[3] == "1":
            raise ValueError("exchange code cannot start with one")

        self.number = number
        self.area_code = number[:3]

    def pretty(self):
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"
