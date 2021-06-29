import lispy


def testAddition():
    assert (lispy.runProg("(+ 3 2 5 8)") == 18)
    assert (lispy.runProg("(+ 1)") == 1)
    assert (lispy.runProg("(+)") == 0)


def testSubtraction():
    assert (lispy.runProg("(- 5)") == -5)
    assert (lispy.runProg("(- 5 3)") == 2)
    assert (lispy.runProg("(- 5 3 1)") == 1)


def testMultiplication():
    assert (lispy.runProg("(* 5 3)") == 15)
    assert (lispy.runProg("(* 5 3 2)") == 30)
    assert (lispy.runProg("(* 5 3)") == 15)
    assert (lispy.runProg("(* 2)") == 2)
    assert (lispy.runProg("(*)") == 1)


def testSomeBuiltins():
    assert (lispy.runProg("(print 3)") == None)
    assert (lispy.runProg("(sum (list 2 3 1))") == 6)
    assert (lispy.runProg("(abs -1)") == 1)
    assert (lispy.runProg("(len \"foo\")") == 3)


def testFunctional():
    assert (lispy.runProg("(foldl + 0 (list 1 2 3))") == 6)
    assert (lispy.runProg("(foldl * 1 (list 1 3 5))") == 15)
    assert (lispy.runProg("(rest (list 1 2))") == [2])
    assert (lispy.runProg("(first (list 1 2))") == 1)


def testDivision():
    assert (lispy.runProg("(/ 12 2)") == 6)
    assert (lispy.runProg("(/ 12 2 3)") == 2)
    assert (lispy.runProg("(/ 3)") == 1 / 3)


def testLambda():
    assert (lispy.runProg("((lambda (x) (+ x 1)) 3)") == 4)
    assert (lispy.runProg("((lambda () 3))") == 3)
    assert (lispy.runProg("(map (lambda (x) (* x 2)) (list 1 2 3 4))") == [
        2, 4, 6, 8
    ])
