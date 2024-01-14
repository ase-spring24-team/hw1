import math

class Sym:
    def __init__(self, s=" ", n=0):
        self.txt = s
        self.at = n
        self.n = 0
        self.has = {}
        self.mode = None
        most = 0

    def add(self, x):
        if x != "?":
            self.n += 1
            if x in self.has:
                self.has[x] += 1
            else:
                self.has[x] = 1
            if self.has[x] > self.most:
                self.most = self.has[x]
                self.mode = x

    def mid(self):
        return self.mode

    def div(self):
        e = 0
        for _, v in self.has.items():
            e -= v / self.n * math.log(v / self.n, 2)
        return e