from pyscipopt import Model

def test_copy():
    # create solver instance
    s = Model()

    # add some variables
    x = s.addVar("x", vtype = 'C', obj = 1.0)
    y = s.addVar("y", vtype = 'C', obj = 2.0)
    s.setObjective(4.0 * y + 10.5, clear = False)

    c = s.addCons(x + 2 * y >= 1.0)

    s2 = Model(sourceModel=s)

    # solve problems
    s.optimize()
    s2.optimize()

    s.writeProblem('s.lp')
    s2.writeProblem('s2.lp')
    assert s.getObjVal() == s2.getObjVal()

if __name__ == "__main__":
    test_copy()
