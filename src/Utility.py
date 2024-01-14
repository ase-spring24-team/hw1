"""
File created by Samuel Kwiatkowski-Martin
For utility purposes such as reading in from a csv file
lines 6-18 are from professor Menzies
"""
import re
import ast
import fileinput

def coerce(s):
  try: return ast.literal_eval(s)
  except Exception: return s

def csv(file="-"):
  with  fileinput.FileInput(None if file=="-" else file) as src:
    for line in src:
      line = re.sub(r'([\n\t\r"\' ]|#.*)', '', line)
      if line: yield [coerce(x) for x in line.split(",")]
