"""
File by Sai Raj Thirumalai
This file is our Sym class, which will contain the Sym data
"""

import math

class Sym:
    def __init__(self, s=" ", n=0):
        """
        Initialization function for the Sym class
        Sets up the column name, column index, number of rows and data aggregates
        :param s: column name, n: column index
        """
        self.txt = s
        self.at = n
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0

    def add(self, x):
        """
        Function that adds a value
        :param x: data value
        """
        if x != "?": # ignore if value is ?
            self.n += 1
            # increase the count of value
            if x in self.has:
                self.has[x] += 1
            else:
                self.has[x] = 1
            # update mode value if needed
            if self.has[x] > self.most:
                self.most = self.has[x]
                self.mode = x

    def mid(self):
        """
        Function that returns the mid (mode) value
        :return: mean
        """
        return self.mode

    def div(self):
        """
        Function that returns the standard deviation
        :return: standard deviation
        """
        e = 0
        for _, v in self.has.items():
            e -= v / self.n * math.log(v / self.n, 2)
        return e