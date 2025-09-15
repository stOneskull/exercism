def append(xs, ys):
    return xs + ys

def concat(lists):
    return [each for liss in lists for each in liss]

def filter(function, xs):
    return [each for each in xs if function(each)]

def length(xs):
    return sum(1 for each in xs)

def map(function, xs):
    return [function(each) for each in xs]

def foldl(function, xs, acc):
    for each in xs:
        acc = function(acc, each)
    return acc

def foldr(function, xs, acc):
    for each in reverse(xs):
        acc = function(acc, each)
    return acc

def reverse(xs):
    return xs[::-1]
