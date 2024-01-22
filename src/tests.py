"""
File created by Samuel Kwiatkowski-Martin
Examples class -- essentially just the testing class
"""
from Data import Data
from Row import Row
from Num import Num
from Sym import Sym
from util import norm, rnd
import util as l
from the import THE, the, SLOTS

tests = {}


def all():
    bad = 0
    good = 0
    for t_name in tests:
        if t_name != "all":
            print("--testing:", t_name)
            if tests[t_name](): # test passed                
                good += 1
                print("Passed")
            else: # test failed
                bad += 1
                print("Failed")
    print("----")
    print("TOTAL:", bad+good)
    print("PASS:", good)
    print("FAIL:", bad)
    exit(bad)

def stats():
    """
    Tests and prints out default for the stats function on auto93.csv
    """
    stat = Data("../data/auto93.csv").stats()
    o_stat = l.o(stat)
    print(o_stat)
    return o_stat == "dict{.N:397 Acc+:15.57 Lbs-:2970.42 Mpg+:23.84}"


def num():
    e = Num()
    for _ in range(1000):
        e.add(norm(10, 2))
    mu, sd = e.mid(), e.div()
    print(rnd(mu, 3), rnd(sd, 3), mu, sd)
    return 9.9 < mu and mu < 10.2 and 3 < sd and sd < 5

def num_2():
    e = Num()
    for _ in range(500):
        e.add(norm(10))
    mu, sd = e.mid(), e.div()
    print(rnd(mu, 3), rnd(sd, 3), mu, sd)
    return 9.9 < mu and mu < 10.2 and 0.9 < sd and sd < 1.2

def sym():
    s = Sym()
    l = [1,1,1,1,2,2,3]
    for x in l:
        s.add(x)
    mode = s.mid()
    e = s.div()
    print(mode, rnd(e, 3))
    return mode == 1 and e > 1.37 and e < 1.38

def egs():
    """
    Prints out all the different tests we can run
    """
    #test_names = ["all", "egs", "help", "sym", "num", "csv", "data", "stats", "oo"]
    test_names = tests.keys()
    for test_name in test_names:
        print("python gate.py -t " + test_name)
    return True

def data():
    n = 0
    d = Data(the.file)
    for i, row in enumerate(d.rows):
        if i % 100 == 0:
            n+= len(row.cells)
            l.oo(row.cells)
    l.oo(d.cols.x[0])
    return n == 32

def csv(src = "../data/auto93.csv"):
    n = 0
    for i, t in enumerate(l.csv(src)):
        if i % 100 == 0:
            n = n + len(t)
        print(i, t)
    return n == 32

def help():
    print(the.__help)
    return True

def oo():
    d = {"a":1,"b":2,"c":3,"d":4}
    print(d)
    print(l.o(d))
    return l.o(d) == "dict{a:1 b:2 c:3 d:4}" 

def oo_2():
    d = {"a":"x","b":"y","c":"z"}
    print(d)
    print(l.o(d))
    return l.o(d) == "dict{a:x b:y c:z}" 

def row():
    """
    Tests the row class
    """
    print("[1, 2, 3] == " + str(Row([1,2,3]).cells))
    return "[1, 2, 3]" == str(Row([1,2,3]).cells)

def row_2():
    print("[5, 4, 3] == " + str(Row([5, 4, 3]).cells))
    return "[5, 4, 3]" == str(Row([5, 4, 3]).cells)

def test_sym_like():
    """
    Tests the like function of Sym class
    """
    wme = SLOTS({"acc": 0, "datas": {}, "tries": 0, "n": 0}) 
    Data("../data/weather.csv",lambda data, t: learn(data,t,wme))
    data = wme.datas["no"]
    prior = (len(data.rows) + the.k) / (wme.n)
    like = data.cols.x[0].like("rainy", prior)
    print("like - ",like)
    return like > 0.36


def test_num_like():
    """
    Tests the like function of Num class
    """
    wme = SLOTS({"acc": 0, "datas": {}, "tries": 0, "n": 0}) 
    Data("../data/weather.csv",lambda data, t: learn(data,t,wme))
    data = wme.datas["yes"]
    prior = (len(data.rows) + the.k) / (wme.n)
    like = data.cols.x[1].like(70, prior)
    print("like - ",like)
    return like > 0.01


def bayes():
    wme = SLOTS({"acc": 0, "datas": {}, "tries": 0, "n": 0}) 
    Data("../data/diabetes.csv",lambda data, t: learn(data,t,wme))
    print("Accuracy:", wme.acc/(wme.tries))
    return wme.acc/(wme.tries) > .64 #.72

def bayes_2():
    wme = SLOTS({"acc": 0, "datas": {}, "tries": 0, "n": 0}) 
    Data("../data/soybean.csv",lambda data, t: learn(data,t,wme))
    print("Accuracy:", wme.acc/(wme.tries))
    return wme.acc/(wme.tries) > .8

def bayes_3():
    wme = SLOTS({"acc": 0, "datas": {}, "tries": 0, "n": 0}) 
    Data("../data/weather.csv",lambda data, t: learn(data,t,wme))
    print(wme.acc/(wme.tries))
    return wme.acc/(wme.tries) > .55

def ascii_table(file_name = None):
    if not file_name: 
        file_name = the.file
    wme = SLOTS({"acc": 0, "datas": {}, "tries": 0, "n": 0}) 
    Data(file_name,lambda data, t: learn(data,t,wme))
    datas = wme.datas 
    print("Number of classes,", len(datas), ",")
    print("Total number of rows,", wme.n, ",")
    print("Class Name, number of rows, percetange")
    for key, values in datas.items():
        print(key,",", len(values.rows),",", len(values.rows) / wme.n)
    return True

def ascii_table_diabetes():
    wme = SLOTS({"acc": 0, "datas": {}, "tries": 0, "n": 0}) 
    Data("../data/diabetes.csv",lambda data, t: learn(data,t,wme))
    datas = wme.datas 
    print("Class Name, number of rows, percetange")
    for key, values in datas.items():
        print(key,",", len(values.rows),",", len(values.rows) / wme.n)
    print("Number of classes,", len(datas), ",")
    print("Total number of rows,", wme.n, ",")
    return True

def ascii_table_soybean():
    wme = SLOTS({"acc": 0, "datas": {}, "tries": 0, "n": 0}) 
    Data("../data/soybean.csv",lambda data, t: learn(data,t,wme))
    datas = wme.datas 
    print("Class Name, number of rows, percetange")
    for key, values in datas.items():
        print(key,",", len(values.rows),",", len(values.rows) / wme.n)
    print("Number of classes,", len(datas), ",")
    print("Total number of rows,", wme.n, ",")
    return True

def global_the():
    t = THE()
    t._set(SLOTS({"a":1, "b": "xyz", "c":True}))
    print({"a":t.a, "b": t.b, "c":t.c})
    t.a = 2
    print({"a":t.a, "b": t.b, "c":t.c})
    return t.a == 2 and t.b == "xyz" and t.c == True

def km():
    """
    This function tests soybean.csv by changing around the hyperparameters k and m
    """
    print(f"Accuracy,K,M")
    for k in range(4):
        for m in range(4):
            #  loop through all the hyperparameters
            the.k = k
            the.m = m
            wme = SLOTS({"acc": 0, "datas": {}, "tries": 0, "n": 0})
            Data("../data/soybean.csv",lambda data, t: learn(data,t,wme))
            print(f"{round(wme.acc / wme.tries, 2)},{k},{m}")
# function to automatically load all functions in this module in test variable
for (k, v) in list(locals().items()):
    if callable(v) and v.__module__ == __name__:
        tests[k] = v

# -- Functions below this will not be loaded as a test

def learn(data, row, my):
    my.n += 1
    kl = row.cells[data.cols.klass.at]
    learned = False
    if my.n > 0:
        my.tries += 1
        my.acc += 1 if kl == row.likes(my.datas) else 0
        my.acc += (1 if kl == row.likes(my.datas)[0] else 0) # usiing [0] as we are comparing 'kl' to only 'out' in Row.likes return
        learned = True
    my.datas.setdefault(kl, Data(data.cols.names))
    test_learn(learned)
    my.datas[kl].add(row)

def test_learn(learned):
    """
    Test function to make sure that learn doesn't add data before it runs likes on the row
    that is trying to be added
    """
    assert learned
    # will throw error if somehow the data gets added before being learned on
def _run(t_name):
    if t_name in tests:
        return tests[t_name]()
    else:
        return None

if __name__ == '__main__':
    #all()
    the._set(SLOTS({"file":"../data/auto93.csv", "__help": "", "m":2, "k":1}))
    # ascii_table("../data/soybean.csv")
    #km()
    # bayes()
    print(bayes_3())
