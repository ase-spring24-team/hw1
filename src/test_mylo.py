"""
File created by Sathiya Narayanan Venkatesan
Examples class -- essentially just the testing mylo related functions 
"""
from the import THE, the, SLOTS
from Data import Data
import util as l

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

def help():
    print(the.__help)
    return True

def far():
    d  = Data.new("../data/auto93.csv")
    far = d.farapart(d.rows)
    print("far1: ", far[0])
    print("far2: ", far[1])
    print("distance = ", far[2])

def egs():
    """
    Prints out all the different tests we can run
    """
    #test_names = ["all", "egs", "help", "sym", "num", "csv", "data", "stats", "oo"]
    test_names = tests.keys()
    for test_name in test_names:
        print("python mylo.py -t " + test_name)
    return True 



# function to automatically load all functions in this module in test variable
for (k, v) in list(locals().items()):
    if callable(v) and v.__module__ == __name__:
        tests[k] = v


def _run(t_name):
    if t_name in tests:
        return tests[t_name]()
    else:
        return None

def dist():
    """
    Prints the first row, sorts all the rows based on their distance to the first row,
    and then prints every 30th row with the distance of each to the first row
    """
    d = Data("../data/auto93.csv")
    r1 = d.rows[0]  # pull out the first row
    rows = r1.neighbors(d)
    for i in range(len(rows)):
        if i%30 == 0:
            print(i, rows[i].cells, round(rows[i].dist(r1, d),2))

if __name__ == '__main__':
    #all()
    the._set(SLOTS({"file":"../data/auto93.csv", "__help": "", "m":2, "k":1, "p":2}))
    dist()
