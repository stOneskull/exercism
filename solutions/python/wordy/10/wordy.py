def answer(quest):
    quest = quest.lstrip('What is').rstrip('?')
    if not quest:
        raise ValueError('syntax error')
    
    opers = {
        '+': 'plus',
        '-': 'minus',
        '*': 'multiplied by',
        '/': 'divided by',
    }
    
    for oper, words in opers.items():
        quest = quest.replace(words, oper)

    quest = quest.split()

    for i, token in enumerate(quest):
        if (i % 2 and token.lstrip('-').isnumeric() or
            i % 2 == 0 and not token.lstrip('-').isnumeric()):
            raise ValueError('syntax error')
        elif i % 2 and token not in opers:
            raise ValueError('unknown operation')

    while len(quest) > 1:
        try:
            op = eval(' '.join(quest[:3]))
        except:
            raise ValueError('syntax error')
        quest = [str(op)] + quest[3:]

    return float(quest.pop())
    