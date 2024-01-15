"""
HW: week 2

OPTIONS:
    -c --cohen  small effect size               = .35
    -f --file   csv data file name              = ../data/auto93.csv
    -h --help   show help                       = False
    -k --k      low class frequency kludge      = 1
    -m --m      low attribute frequency kludge  = 2
    -s --seed   random number seed              = 31210
    -t --test   start up action                 = help
"""

import util as l


def run(x):
    print(x)


the = l.settings(__doc__)
run(l.cli(the).test)
