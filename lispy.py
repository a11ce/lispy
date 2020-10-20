from initDict import symDict

def evaluate(exp):
    #print(exp)
    if type(exp) == tuple or type(exp) == list:
        return evalProc(exp)
    else:
        return evalPrimitive(exp)

def evalProc(exp):
    subVals = [evaluate(x) for x in exp]
    #print(subVals)
    return subVals[0](*subVals[1:])

def evalPrimitive(exp):
    #print(exp)
    if exp in symDict:
        return symDict[exp]
    if callable(exp):
        return exp
    return eval(exp)

def parse(progL):
    if len(progL) == 0:
        raise SyntaxError()
    curToken = progL.pop(0)
    if curToken == '(':
        L = []
        while progL[0] != ')':
            L.append(parse(progL))
        progL.pop(0)
        return L
    elif curToken == ')':
        raise SyntaxError('unexpected )')
    else:
        return curToken

def runProg(progS):
    parsed = parse(progS.replace('(', ' ( ').replace(')', ' ) ').split())
    #print(parsed)
    return evaluate(parsed)