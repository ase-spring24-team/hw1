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
import gate


def stats():
    """
    Tests and prints out default for the stats function on auto93.csv
    """
    print(Data("../data/auto93.csv").stats())


def num():
    e = Num()
    for _ in range(1000):
        e.add(norm(10, 2))
    mu, sd = e.mid(), e.div()
    print(rnd(mu, 3), rnd(sd, 3), mu, sd)
    return 9.9 < mu and mu < 10.2 and 3 < sd and sd < 5

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
    test_names = ["all", "egs", "help", "sym", "num", "csv", "data", "stats", "oo"]
    for test_name in test_names:
        print("python gate.py -t " + test_name)

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
    print(gate.the.help)

def oo():
    d = {"a":1,"b":2,"c":3,"d":4}
    print(d)
    print(l.o(d))
    return l.o(d) == "dict{a:1 b:2 c:3 d:4}" 


the = l.SLOTS({"file":"../data/auto93.csv"})


def row():
    """
    Tests the row class
    """
    print("[1, 2, 3] == " + str(Row([1,2,3]).cells))

def all():
    """
    Tests all test functions
    """
    stats()
    print(num())
    egs()
    the = l.SLOTS({"file": "../data/auto93.csv"})
    print(data())
    oo()
    row()
    sym()
    csv()
    help()

all()