class Num:
    def __init__(self, s=" ", n=0):
        self.txt = s
        self.at = n
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = -1e30
        self.lo = 1e30
        heaven = 0 if s.endswith("-") else 1

    def add(self, x):
        if x != "?":
            self.n += 1
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        if self.n < 2:
            return 0
        else:
            return self.m2 / (self.n - 1)

    def norm(self, x):
        if x == "?":
            return x
        else:
            (x - self.lo) / (self.hi - self.lo + 1e-30)
