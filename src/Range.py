"""
File by Sathiya Narayanan Venkatesan
This file is our Range class, distinguish sets of rows (stored in `rowss`)
"""

from collections import defaultdict
import util as l

class Range:
    def __init__(self, at, txt, lo, hi = None):
        """
        Initialization function for the Range class
        Sets up the column name, column index, range of x and range of y
        :param s: column name, n: column index
        """
        self.txt = txt
        self.at = at
        self.x = { lo: lo, hi : hi if hi else lo}
        self.y = defaultdict(int)

    def add(self, x, y):
        """
        add function for the Range class
        adds a range to the existing range
        """
        self.x["lo"] = min(self.x["lo"], x)
        self.x["hi"] = min(self.x["hi"], x)
        self.y[y] = self.y[y] + 1 

    def show(self):
        """
        print function for the Range class
        prints the range based on the data
        """
        lo, hi, s = self.x["lo"], self.x["hi"], self.txt
        if lo == int("-inf"):
            return " {} < {} ".format(s, hi)
        if hi == int("inf"):
            return " {} >= {} ".format(s, lo)
        if lo == hi:
            return " {} == {} ".format(s, lo)
        return " {} <= {} < {}".format(lo, s, hi)

    def score(self, goal, LIKE, HATE):
        """
        score function for the Range class
        returns the score from the util score method
        """
        return l.score(self.y, goal, LIKE, HATE)
    
    def merge(self, other):
        """
        merge function for the Range class
        merge a range with the existing range
        """
        both = Range(self.at, self.txt, self.x["lo"])
        both.x["lo"] = min(self.x["lo"], other.x["lo"])
        both.x["hi"] = max(self.x["hi"], other.x["hi"])
        for _, t in self.y.items():
            for k, v in enumerate(t):
                both.y[k] = both.y[k] + v 
        for _, t in other.y.items():
            for k, v in enumerate(t):
                both.y[k] = both.y[k] + v 
        return both
    
    def merged(self, other, toofew):
        """
        merged function for the Range class
        check if the range is interesting and merge if it is
        """
        both = self.merge(other)
        e1, n1 = l.entropy(self.y)
        e2, n2 = l.entropy(other.y)
        if n1 <= toofew or n2 <= toofew:
            return both
        if l.entropy(both.y) <= (n1*e1 + n2*e2) / (n1+n2):
            return both

