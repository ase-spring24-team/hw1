"""
File by Samuel Kwiatkowski-Martin
This file is our data class, which will contain and process columns and rows
"""
from Row import Row # Imports the Row class from the Row file
from Utility import csv # Imports the csv function from utility
from Cols import Cols  # Imports the Cols class
from Sym import Sym
from Num import Num

class Data:
    def __init__(self, src):
        """
        Initialization function for the data class
        Sets up rows and columns and calls to read in required values
        :param src: Either the csv filename or a list of rows
        """
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            # checks if src is a string
            self.process_file(src)

    def process_file(self, src):
        """
        Function that process the src file
        :param src: the csv file to be processed
        :return: None
        """
        for row in csv("../data/auto93.csv"):
            self.add(row)

    def add(self, t):
        """
        Function that adds rows and columns from the read csv
        :param t: t is the row to be added and should be passed as an array
        :return: None
        """
        row = Row(t)
        if self.cols is None:
            self.cols = Cols(row)
            # the following is not included in his lua code, but I believe we need it
            self.rows.append((self.cols))
        else:
            self.rows.append(self.cols.add(row))

    def stats(self):
        pass

    def mid(self, cols):
        """
        Function returns the means and modes of all or a selection of columns
        :param cols: A selection of columns if you wouldn't like to see all of them
        :return: Return an array that represents the means/modes of whatever columns were selected
        """
        u = [] ## our table
        if cols is not None:
            for x in cols:
                u.append(u.mid)  # u.mid should automatically return either sym.mid or num.mid
        else:
            # else we just go through all of self.cols
            for x in self.cols:
                u.append(u.mid)
        return Row(u)  # returning an array of means/modes

    def div(self, cols):
        """
        Function returns the standard deviation or entropy of all, or a selection of columns
        :param cols: A selection of columns if you wouldn't like to see all of them
        :return: Return an array that represents the sd/entropy of whatever columns were selected
        """
        u = []  ## our table
        if cols is not None:
            for x in cols:
                u.append(u.div)  # u.mid should automatically return either sym.div or num.div
        else:
            # else we just go through all of self.cols
            for x in self.cols:
                u.append(u.div)
        return Row(u)  # returning an array of sds/entropys
