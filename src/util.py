"""
File created by Samuel Kwiatkowski-Martin
For util purposes such as reading in from a csv file
lines 6-18 are from professor Menzies
"""
import re
import ast
import sys
import random
import math
import fileinput


def coerce(val):
    try:
        return ast.literal_eval(val)
    except:
        return val.strip()


def csv(file="-"):
    with fileinput.FileInput(None if file == "-" else file) as src:
        for line in src:
            line = re.sub(r'([\n\t\r"\' ]|#.*)', "", line)
            if line:
                yield [coerce(x) for x in line.split(",")]


class SLOTS(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__


def settings(help_doc=__doc__):
    s = SLOTS(
        **{m[1]: coerce(m[2]) for m in re.finditer(r"--(\w+)[^=]*=\s*(\S+)", help_doc)}
    )
    s.__help = help_doc
    return s


def cli(t):
    for k, v in t.items():
        v = str(v)
        for i, s in enumerate(sys.argv):
            if s == "-" + k[0] or s == "--" + k:
                v = "False" if v == "True" else ("True" if v == "False" else sys.argv[i+1])
                t[k] = coerce(v)
    return t

def norm(mu = 0, sd = 1):
    R = random.random
    return mu + sd * math.sqrt(-2 * math.log(R())) * math.cos(2 * math.pi * R())

def rnd(n, ndecs = 2):
    if type(n) != int and type(n) != float:
        return n
    if math.floor(n) == n:
        return n
    mult = 10 ** ndecs
    return math.floor(n * mult + 0.5) / mult

def oo(x): 
    print(o(x)); 
    return x

def o(x): 
    if type(x) == int or type(x) == float:
        return str(x)
    if type(x) == str:
        return x
    if type(x) == list:
        return str(x)
    elif hasattr(x, "items"):    
        return x.__class__.__name__ +"{"+ (" ".join([f"{k}:{v}" for k,v in sorted(x.items()) if k[0]!="_"]))+"}"
    else:
        return x.__class__.__name__ +"{"+ (" ".join([f"{k}:{v}" for k,v in sorted(vars(x).items()) if k[0]!="_"]))+"}"