"""
File created by Samuel Kwiatkowski-Martin
For util purposes such as reading in from a csv file
lines 6-18 are from professor Menzies
"""
import re
import ast
import sys
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