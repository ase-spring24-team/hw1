"""
File by Samuel Kwiatkowski-Martin
This file is our data class, which will contain and process columns and rows
"""
from Row import Row ## Imports the Row class from the Row file
from Utility import csv ## Imports the csv function from utility
from Cols import Cols  ## Imports the Cols class

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
            ## checks if src is a string
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
            ## the following is not included in his lua code but I believe we need it
            self.rows.append((self.cols))
        else:
            self.rows.append(self.cols.add(row))
