import Num
import Sym

class Cols:
    def __init__(self, row):
        self.x = []
        self.y = []
        self.all = []
        self.klass 
        self.col 
        for key, value in row:
            if value.isupper():
                col = Num(value, key)
            else:
                col = Sym(value, key)
            self.all.append(col)
            if not value.endswith("X"):
                if value.endswith("!"):
                    klass = col
                if value.endswith("!") or value.endswith("+") or value.endswith("-"):
                    self.x[key] = col
                else:
                    self.y[key] = col
    
    def add(self, row):
        for _, cols in enumerate([self.x, self.y]):
            for _, col in enumerate(cols):
                col.add(row.cells[col.at])
            