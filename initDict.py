def rest(l):
    return l[1:]

def first(l):
    return l[0]

def foldl(f, base, l):
    if not l:
        return base
    else:
        return f(first(l), foldl(f, base, rest(l) ))

def realPlus(a, b):
    return a + b

def realSub(a, b):
    return a - b

def realMul(a, b):
    return a * b
    
symDict = {
    '+': lambda *x: foldl(realPlus, 0, x),
    '-': lambda *x: first(x) - foldl(realPlus, 0, rest(x)) if len(x) > 1 else -1 * x[0],
    '*': lambda *x: foldl(realMul, 1, x),
    '/': lambda *x: first(x) / foldl(realMul, 1, rest(x)) if len(x) > 1 else 1/x[0],
    #'/': lambda *x: division(*x),
    #'%': lambda *x: sum(x),
    #'**': lambda *x: sum(x),
    #'//': lambda *x: sum(x),
    'list': lambda *x: list(x),
}