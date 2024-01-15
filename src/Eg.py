"""
File created by Samuel Kwiatkowski-Martin
Examples class -- essentially just the testing class
"""
from Data import Data
from Num import Num
from util import norm, rnd

def stats():
    print(Data("../data/auto93.csv").stats())

def num():
    e = Num()
    for _ in range(1000):
        e.add(norm(10, 2))
    mu, sd = e.mid(), e.div()
    print(rnd(mu, 3), rnd(sd, 3), mu, sd)
    return 9.9 < mu and mu < 10.2 and 3 < sd and sd < 5


stats()
print(num())
