import re


def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle)

    addends, result = words[:-1], words[-1]

    rev_addends = [word[::-1] for word in addends]
    rev_result = result[::-1]

    first_letters = {word[0] for word in words if len(word) > 1}

    solution = {}

    used_digits = [False] * 10

    max_len = max(len(word) for word in words)


    def backtrack(column, carry):
        if column == max_len:
            return solution if carry == 0 else None

        words = rev_addends + [rev_result]
        letters = set(word[column] for word in words if column < len(word)) 

        letters_to_assign = sorted(
            [letter for letter in letters if letter not in solution]
        )


        def assign_letters(letters):
            if not letters:
                addend_sum = sum(
                    solution[word[column]] for word in rev_addends 
                    if column < len(word)
                )
                column_sum = addend_sum + carry

                result_char = rev_result[column]

                if solution[result_char] == column_sum % 10:
                    return backtrack(column + 1, column_sum // 10)
                return None

            letter = letters[0]

            for digit in range(10):
                if not used_digits[digit]:
                    if digit == 0 and letter in first_letters:
                        continue

                    solution[letter] = digit
                    used_digits[digit] = True
                    
                    res = assign_letters(letters[1:])
                    if res: return res

                    used_digits[digit] = False
                    del solution[letter]

        return assign_letters(letters_to_assign)


    return backtrack(0, 0)
