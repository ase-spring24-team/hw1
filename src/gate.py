"""
Automated Software Engineering - Homework Week 2
by:
    Sai Raj Thirumalai
    Sam Kwiatkowski-Martin
    Sathiya Narayanan Venkatesan

USAGE:
  python gate.py [OPTIONS]

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
import tests as eg
import random
from the import set_the

def run(the):
    if the.help:
      print(the.__help)
      exit(0)
    set_the(the)
    random.seed(the.seed)
    oops = False if eg._run(the.test) else True

    exit(oops)

the = l.settings(__doc__)
run(l.cli(the))
