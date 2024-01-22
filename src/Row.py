"""
File by Samuel Kwiatkowski-Martin
This file is our row class
"""
import math
from the import the

class Row:
    """
    Initializes the row using a passed array
    param t: the array the represents the row we care about
    """
    def __init__(self, t):
        self.cells = t

    def likes(self, datas):
        n, nHypotheses = 0, 0
        most = out = None
        for (k, data) in datas.items():
            n += len(data.rows)
            nHypotheses += 1
        for (k, data) in datas.items():
            tmp = self.like(data, n, nHypotheses)
            if most is None or tmp > most:
                most, out = tmp, k
        return out, most