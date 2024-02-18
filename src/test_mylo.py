"""
File created by Sathiya Narayanan Venkatesan
Examples class -- essentially just the testing mylo related functions 
"""
from the import THE, the, SLOTS
from Data import Data
from Num import Num
from Sym import Sym
import util as l

tests = {}


def all():
    bad = 0
    good = 0
    for t_name in tests:
        if t_name != "all":
            print("--testing:", t_name)
            if tests[t_name](): # test passed                
                good += 1
                print("Passed")
            else: # test failed
                bad += 1
                print("Failed")
    print("----")
    print("TOTAL:", bad+good)
    print("PASS:", good)
    print("FAIL:", bad)
    exit(bad)

def help():
    print(the.__help)
    return True

def far():
    d  = Data("../data/auto93.csv")
    far = d.farapart(d.rows)
    print("far1: ", l.o(far[0]))
    print("far2: ", l.o(far[1]))
    print("distance = ", far[2])
    return l.rnd(far[2]) == 85

def egs():
    """
    Prints out all the different tests we can run
    """
    #test_names = ["all", "egs", "help", "sym", "num", "csv", "data", "stats", "oo"]
    test_names = tests.keys()
    for test_name in test_names:
        print("python mylo.py -t " + test_name)
    return True 

def test_row_neighbors0():
    d = Data("../data/auto93.csv")
    r1 = d.rows[0]
    r2 = r1.neighbors(d)[0]
    print(l.o(r1), "==", l.o(r2))
    return r1==r2

def test_row_neighbors1():
    d = Data("../data/auto93.csv")
    r1 = d.rows[0]
    r2 = r1.neighbors(d)[1]
    print(l.o(r1), "closest", l.o(r2))
    return r1 != r2

def test_row_dist():
    d = Data("../data/auto93.csv")
    r1 = d.rows[0]
    r2 = r1.neighbors(d)[1]
    distance  = r2.dist(r1, d)
    print(l.o(r1), l.o(r2), l.rnd(distance))
    return distance == 0

def dist():
    """
    Prints the first row, sorts all the rows based on their distance to the first row,
    and then prints every 30th row with the distance of each to the first row
    """
    d = Data("../data/auto93.csv")
    r1 = d.rows[0]  # pull out the first row
    rows = r1.neighbors(d)
    for i in range(len(rows)):
        if i%30 == 0:
            print(i+1, rows[i].cells, round(rows[i].dist(r1, d),2))

def test_sym_dist_both_unknown():
    """
    Tests that the sym.dist function is working as expected when 2 "?" values are input
    """
    n = Sym()
    print(n.dist("?","?") == 1)
    return n.dist("?","?") == 1


def test_sym_dist_one_unknown():
    """
    Tests that sym.dist works as expected when only one value is unknown
    """
    n = Sym()
    print(n.dist("A","?") == 1)
    return n.dist("A","?") == 1

def test_sym_dist_both_known_and_equal():
    """
    Tests that sym dist works when both x and y are known and are equal
    """
    n = Sym()
    print(n.dist("A","A") == 0)
    return n.dist("A","A") == 0

def test_sym_dist_both_known_and_not_equal():
    """
    Tests that sym dist works when both x and y are known and are not equal
    """
    n = Sym()
    print(n.dist("A","B") == 1)
    return n.dist("A","B") == 1

def test_num_dist_both_unknown():
    """
    Tests that the num.dist function is working as expected when 2 "?" values are input
    """
    n = Num()
    assert n.dist("?","?") == 1

def test_num_dist_one_unknown():
    """
    Tests that num.dist works as expected when only one value is unknown
    """
    n = Num()
    for i in range(1, 11):
        n.add(i)  # adding nums from 1 to 10
    assert n.dist("?", 5) == 1-(4/9+1E-30)  # should be the exact output in this case
    assert n.dist(5, "?") == 1-(4/9+1E-30)  #
    assert n.dist("?", 8) == 7/9+1E-30
    assert n.dist(8, "?") == 7/9+1E-30

def test_num_dist_both_known():
    """
    Tests that num dist works when both x and y are known
    """
    n = Num()
    for i in range(1, 11):
        n.add(i)  # adding nums from 1 to 10
    assert n.dist(6, 5) == (5 / 9 + 1E-30) - (4 / 9 + 1E-30)  # should be the exact output
    assert n.dist(5, 6) == abs((4 / 9 + 1E-30)-(5 / 9 + 1E-30))

def half():
    d = Data("../data/auto93.csv")
    lefts, rights, left, right, C, cut, evals = d.half(d.rows)
    print(len(lefts), len(rights), l.o(left.cells), l.o(right.cells), l.o(C), l.o(cut), evals)

def tree():
    t, evals = Data("../data/auto93.csv").tree(True)
    t.show()
    print(evals)

# function to automatically load all functions in this module in test variable
for (k, v) in list(locals().items()):
    if callable(v) and v.__module__ == __name__:
        tests[k] = v

# -- Functions below this will not be loaded as a test

def _run(t_name):
    if t_name in tests:
        return tests[t_name]()
    else:
        return None

if __name__ == '__main__':
    #all()
    the._set(SLOTS({"file":"../data/auto93.csv", "__help": "", "m":2, "k":1, "p":2}))
    tree()
    """
    test_sym_dist_both_unknown()
    test_sym_dist_one_unknown()
    test_sym_dist_both_known_and_equal()
    test_sym_dist_both_known_and_not_equal()
    """
