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
    
    def like(self, data, n, nHypotheses):
        prior = (len(data.rows) + the.k) / (n + the.k *nHypotheses)
        out = math.log(prior)
        for col in data.cols.x:
            v = self.cells[col.at]
            if v != "?":
                inc = col.like(v, prior)
                out = out + (math.log(inc) if inc != 0 else 0)
        return math.exp(1) ** out
