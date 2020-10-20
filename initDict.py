symDict = {
    '+': lambda *x: 0 if len(x) == 0 else (x[0] if len(x) == 1 else x[0] + symDict['+'](*x[1:])),
    '-': lambda *x: -1 * x[0] if len(x) == 1 else x[0] - symDict['+'](*x[1:]),
    '*': lambda *x: 1 if len(x) == 0 else (x[0] if len(x) == 1 else x[0] *  symDict['*'](*x[1:])),
    #'/': lambda *x: x[0] if len(x) == 1 else x[0] / symDict['/'](*x[1:]),
    #'/': lambda *x: division(*x),
    #'%': lambda *x: sum(x),
    #'**': lambda *x: sum(x),
    #'//': lambda *x: sum(x),

    'list': lambda *x: list(x)
}