"""
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
from Data import Data

def run(the):
    if the.help or the.test == 'help':
      print(the.__help)
      exit(0)
    
    data = Data(the.file)

    if the.test == 'stats':
      print(data.stats(cols='all'))





the = l.settings(__doc__)
run(l.cli(the))
