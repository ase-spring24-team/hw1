"""
File created by Samuel Kwiatkowski-Martin
Examples class -- essentially just the testing class
"""
from Data import Data

def stats():
    print(Data("../data/auto93.csv").stats())

stats()
