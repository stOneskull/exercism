def junk2book(junk):
    book = {}
    units = len(junk[0]) // 3
    chop = 0
    for unit in range(units):
        book[unit] = [line[chop:chop+3] for line in junk]
        chop += 3

    return book


digitbook = junk2book(
    [
    " _     _  _     _  _  _  _  _ ",
    "| |  | _| _||_||_ |_   ||_||_|",
    "|_|  ||_  _|  | _||_|  ||_| _|",
    "                              ",
    ]
)

def readbook(book):
    output = ''
    
    for entry in book:
        for digit, code in digitbook.items():
            if book[entry] == code:
                output += str(digit)
                break
        else:
            output += '?'

    return output


def convert(junk):
    if len(junk) % 4:
        raise ValueError('Number of input lines is not a multiple of four')
    if any(len(line) % 3 for line in junk):
        raise ValueError('Number of input columns is not a multiple of three')
    
    books = []
    ranks = len(junk) // 4
    chop = 0
    for rank in range(ranks):
        books.append(junk2book(junk[chop:chop+4]))
        chop += 4

    return ','.join(readbook(book) for book in books)
