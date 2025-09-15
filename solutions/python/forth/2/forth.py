# Froth Forth

from operator import add, sub, mul, floordiv


class StackUnderflowError(Exception):
    pass


class Stack:
    builtins = ['dup', 'drop', 'swap', 'over']
    opers = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': floordiv,
    }

    def __init__(self):
        self.stack = []
        self.funcs = {}

    def dup(self):
        self.stack.append(self.stack[-1])

    def drop(self):
        self.stack.pop()

    def swap(self):
        self.stack.append(self.stack.pop(-2))

    def over(self):
        self.stack.append(self.stack[-2])

    def check(self, words):
        word = words[0]
        return (
            words if word not in self.funcs
            else self.funcs[word] + words[1:]
        )

    def makefunc(self, words):
        words = words[1:-1]
        funcname = words.pop(0)
        if funcname[0].isnumeric() or funcname[0] == '-':
            raise ValueError('illegal operation')
        self.funcs[funcname] = self.check(words)

    def feed(self, words):
        while words:
            words = self.check(words)
            word = words.pop(0)

            if word.isnumeric():
                self.stack.append(int(word))

            elif word in self.builtins:
                try:
                    exec(f'self.{word}()')
                except IndexError:
                    raise StackUnderflowError('Insufficient number of items in stack')


            elif word in self.opers:
                try:
                    self.stack.append(
                        self.opers[word](
                            self.stack.pop(-2),
                            self.stack.pop()
                        )
                    )
                except ZeroDivisionError:
                    raise ZeroDivisionError('divide by zero')
                except IndexError:
                    raise StackUnderflowError('Insufficient number of items in stack')
                
            elif word.lstrip('-').isnumeric():
                self.stack.append(int(word))

            else:
                raise ValueError('undefined operation')


def evaluate(input_data):
    stack = Stack()

    for line in input_data:
        words = line.lower().split()

        if words[0] == ':':
            stack.makefunc(words)
        else:
            stack.feed(words)

    return stack.stack
