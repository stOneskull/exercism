brace = {
    '(': ')',
    '[': ']',
    '{': '}',
    }

def is_paired(line):
    we = []

    for you in line:
        if you in brace:
            we.append(brace[you])
        elif you in brace.values():
            if not we or we.pop() != you:
                return False

    return we == []
