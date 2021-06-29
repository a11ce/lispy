from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Symbol:
    symbol: str


def first(l):
    return l[0]


def rest(l):
    return l[1:]


def foldl(f, base, l):
    if not l:
        return base
    else:
        return f(first(l), foldl(f, base, rest(l)))


def define(symbol, exp):
    globalDict[symbol] = exp
    return exp


def realPlus(a, b):
    return a + b


def realMul(a, b):
    return a * b


globalDict = {
    '+':
    lambda *x: foldl(realPlus, 0, x),
    '-':
    lambda *x: first(x) - foldl(realPlus, 0, rest(x))
    if len(x) > 1 else -1 * x[0],
    '*':
    lambda *x: foldl(realMul, 1, x),
    '/':
    lambda *x: first(x) / foldl(realMul, 1, rest(x))
    if len(x) > 1 else 1 / x[0],
    'list':
    lambda *x: list(x),
    'map':
    lambda f, x: list(map(f, x)),
    'foldl':
    lambda *x: foldl(*x),
    'first':
    lambda *x: first(*x),
    'rest':
    lambda *x: rest(*x),
    'def':
    lambda *x: define(*x),
}
