from initDefs import globalDict, Symbol
from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Lambda:
    args: list
    body: list

    def __call__(self, *passedArgs):
        localDict = dict(zip(self.args, passedArgs))
        return evaluate(self.body, scopedDict=globalDict | localDict)


def evaluate(exp, scopedDict=globalDict):
    #print(exp)
    if type(exp) == tuple or type(exp) == list:
        return evalProc(exp, scopedDict=scopedDict)
    else:
        return evalPrimitive(exp, scopedDict)


def evalProc(exp, scopedDict=globalDict):

    if exp[0] == "lambda":
        return Lambda(exp[1], exp[2])
    subVals = [evaluate(x, scopedDict=scopedDict) for x in exp]
    #print(subVals)
    #print(subVals)

    return subVals[0](*subVals[1:])


def evalPrimitive(exp, scopedDict):
    if Symbol(exp) in scopedDict:
        return scopedDict[Symbol(exp)]
    if exp in scopedDict:
        return scopedDict[exp]
    if callable(exp):
        return exp
    try:
        return eval(exp)
    except NameError:
        #print(globalDict)
        return Symbol(exp)


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


def repl():  # pragma: no cover
    print("lispy v0")
    while True:
        print(runProg(input("> ")))


if __name__ == "__main__":  # pragma: no cover
    repl()
