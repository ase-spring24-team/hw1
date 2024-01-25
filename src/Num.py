"""
File by Sai Raj Thirumalai
This file is our Num class, which will contain the numeric data
"""

class Num:
    def __init__(self, s=" ", n=0):
        """
        Initialization function for the Num class
        Sets up the column name, column index, number of rows and data aggregates
        :param s: column name, n: column index
        """
        self.txt = s
        self.at = n
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = -1E30
        self.lo = 1E30
        self.heaven = 0 if s.endswith("-") else 1

    def add(self, x):
        """
        Function that adds a value
        :param x: data value
        """
        if x != "?": # ignore if value is ?
            self.n += 1
            # calculate mean value
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            # update high and low values
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mid(self):
        """
        Function that returns the mid (mean) value
        :return: mean
        """
        return self.mu

    def div(self):
        """
        Function that returns the standard deviation
        :return: standard deviation
        """
        if self.n < 2:
            return 0
        else:
            return (self.m2 / (self.n - 1)) ** 0.5

    def norm(self, x):
        """
        Function that returns the normalized value
        :param x: data value
        :return: normalized value
        """
        if x == "?":
            return x
        else:
            (x - self.lo) / (self.hi - self.lo + 1E-30)

    # Likelihood
    def like(self, x, _):
        mu, sd = self.mid(), (self.div() + 1E-30)
        nom = 2.718 ** (-.5*(x - mu)**2 / (sd **2))
        denom = (sd*2.5 + 1E-30)
        return nom/denom

    def d2h(self, data):
        """
        Function that returns the d2h (distance to heaven) value
        :return: d2h
        """
        d, n = 0, 0
        for col in data.cols.y:
            n += 1
            d += abs(col.heaven - col.norm(self.cells[col.at])) ** 2
