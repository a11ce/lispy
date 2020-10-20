import lispy

def testAddition():
    assert(lispy.runProg("(+ 3 2 5 8)") == 18)
    assert(lispy.runProg("(+ 1)") == 1)
    assert(lispy.runProg("(+)") == 0)

def testSubtraction():
    assert(lispy.runProg("(- 5)") == -5)
    assert(lispy.runProg("(- 5 3)") == 2)
    assert(lispy.runProg("(- 5 3 1)") == 1)


def testMultiplication():
    assert(lispy.runProg("(* 5 3)") == 15)
    assert(lispy.runProg("(* 5 3 2)") == 30)
    assert(lispy.runProg("(* 5 3)") == 15)
    assert(lispy.runProg("(* 2)") == 2)
    assert(lispy.runProg("(*)") == 1)

#def testDivision():
    #assert(lispy.runProg("(/ 12 2)") == 6)
    #assert(lispy.runProg("(/ 12 2 3)") == 2)
    #assert(lispy.runProg("(/ 3)") == 1/3)