"""
File created by Samuel Kwiatkowski-Martin
Examples class -- essentially just the testing class
"""
from Data import Data
from Num import Num
from util import norm, rnd
import util as l


def stats():
    print(Data("../data/auto93.csv").stats())


def num():
    e = Num()
    for _ in range(1000):
        e.add(norm(10, 2))
    mu, sd = e.mid(), e.div()
    print(rnd(mu, 3), rnd(sd, 3), mu, sd)
    return 9.9 < mu and mu < 10.2 and 3 < sd and sd < 5

def egs():
    """
    Prints out all the different tests we can run
    """
    test_names = ["all", "egs", "help", "sym", "num", "csv", "data", "stats"]
    for test_name in test_names:
        print("lua gat.lua -t " + test_name)

def data(the):
    n = 0
    d = Data(the.file)
    for i, row in enumerate(d.rows):
        if i % 100 == 0:
            n+= len(row.cells)
            l.oo(row.cells)
    l.oo(d.cols.x[0])
    return n == 32


stats()
print(num())
egs()
print(data(l.SLOTS({"file":"../data/auto93.csv"})))
