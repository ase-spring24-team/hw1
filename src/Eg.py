"""
File created by Samuel Kwiatkowski-Martin
Examples class -- essentially just the testing class
"""
from Data import Data
from Row import Row
from Num import Num
from Sym import Sym
from util import norm, rnd
import util as l

tests = {}
the = l.SLOTS({"file":"../data/auto93.csv", "help": ""}) #Will be overridden when the is loaded by gate.py


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

def stats():
    """
    Tests and prints out default for the stats function on auto93.csv
    """
    stat = Data("../data/auto93.csv").stats()
    o_stat = l.o(stat)
    print(o_stat)
    return o_stat == "dict{.N:397 Acc+:15.57 Lbs-:2970.42 Mpg+:23.84}"


def num():
    e = Num()
    for _ in range(1000):
        e.add(norm(10, 2))
    mu, sd = e.mid(), e.div()
    print(rnd(mu, 3), rnd(sd, 3), mu, sd)
    return 9.9 < mu and mu < 10.2 and 3 < sd and sd < 5

def num_2():
    e = Num()
    for _ in range(500):
        e.add(norm(10))
    mu, sd = e.mid(), e.div()
    print(rnd(mu, 3), rnd(sd, 3), mu, sd)
    return 9.9 < mu and mu < 10.2 and 0.9 < sd and sd < 1.2

def sym():
    s = Sym()
    l = [1,1,1,1,2,2,3]
    for x in l:
        s.add(x)
    mode = s.mid()
    e = s.div()
    print(mode, rnd(e, 3))
    return mode == 1 and e > 1.37 and e < 1.38

def egs():
    """
    Prints out all the different tests we can run
    """
    #test_names = ["all", "egs", "help", "sym", "num", "csv", "data", "stats", "oo"]
    test_names = tests.keys()
    for test_name in test_names:
        print("python gate.py -t " + test_name)
    return True

def data():
    n = 0
    d = Data(the.file)
    for i, row in enumerate(d.rows):
        if i % 100 == 0:
            n+= len(row.cells)
            l.oo(row.cells)
    l.oo(d.cols.x[0])
    return n == 32

def csv():
    n = 0
    for i, t in enumerate(l.csv("../data/auto93.csv")):
        if i % 100 == 0:
            n = n + len(t)
        print(i, t)
    return n == 32

def help():
    print(the.help)
    return True

def oo():
    d = {"a":1,"b":2,"c":3,"d":4}
    print(d)
    print(l.o(d))
    return l.o(d) == "dict{a:1 b:2 c:3 d:4}" 

def oo_2():
    d = {"a":"x","b":"y","c":"z"}
    print(d)
    print(l.o(d))
    return l.o(d) == "dict{a:x b:y c:z}" 

def row():
    """
    Tests the row class
    """
    print("[1, 2, 3] == " + str(Row([1,2,3]).cells))
    return "[1, 2, 3]" == str(Row([1,2,3]).cells)

def row_2():
    print("[5, 4, 3] == " + str(Row([5, 4, 3]).cells))
    return "[5, 4, 3]" == str(Row([5, 4, 3]).cells)

# function to automatically load all functions in this module in test variable
for (k, v) in list(locals().items()):
    if callable(v) and v.__module__ == __name__:
        tests[k] = v

def _load(t):
    the = t

def _run(t_name):
    if t_name in tests:
        return tests[t_name]()
    else:
        return None

if __name__ == '__main__':
    all()