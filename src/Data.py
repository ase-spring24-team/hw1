"""
File by Samuel Kwiatkowski-Martin
This file is our data class, which will contain and process columns and rows
"""
from Row import Row # Imports the Row class from the Row file
from utility import csv # Imports the csv function from utility
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
        for row in csv(src):
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

    def stats(self, cols="y", fun="mid", ndivs=2):
        """
        Computes the requested stats for whichever column requested
        :param cols: A str that is the cols we would like stats on
        :param fun: A str that determines which stat you would like, mean/standard deviation
        :param ndivs: An int giving us the number of precsion points in our returned stats
        :return: A dictionary that holds column names as keys, and stat values as values
        """
        u = {}  # a dictionary to be returned

        if cols == "y":
            if fun == "mid":
                for col in self.cols.y:
                    #  Remember, col here is either a NUM or SYM object
                    u[col.txt] = round(col.mid, ndivs)
            elif fun == "div":
                for col in self.cols.y:
                    u[col.txt] = round(col.div, ndivs)
            elif fun == "small":
                pass #  doesn't need to be implemented yet
        elif cols == "x":
            if fun == "mid":
                for col in self.cols.x:
                    #  Remember, col here is either a NUM or SYM object
                    u[col.txt] = round(col.mid, ndivs)
            elif fun == "div":
                for col in self.cols.x:
                    u[col.txt] = round(col.div, ndivs)
            elif fun == "small":
                pass #  doesn't need to be implemented yet
        elif cols == "all":
            if fun == "mid":
                for col in self.cols.all:
                    #  Remember, col here is either a NUM or SYM object
                    u[col.txt] = round(col.mid, ndivs)
            elif fun == "div":
                for col in self.cols.all:
                    u[col.txt] = round(col.div, ndivs)
            elif fun == "small":
                pass #  doesn't need to be implemented yet
        else:
            #  This is our strange scenario where the str input in lets say an individual column
            if fun == "mid":
                for col in self.cols.all:
                    if col.txt in cols:
                        #  Remember, col here is either a NUM or SYM object
                        u[col.txt] = round(col.mid, ndivs)
            elif fun == "div":
                for col in self.cols.all:
                    if col.txt in cols:
                        u[col.txt] = round(col.div, ndivs)
            elif fun == "small":
                pass #  doesn't need to be implemented yet
        return u

    def mid(self, cols):
        """
        Function returns the means and modes of all or a selection of columns
        :param cols: A str that tells the function which columns to calculate on
        :return: Return an array that represents the means/modes of whatever columns were selected
        """
        u = []  # an array to be returned

        if cols == "y":
            for col in self.cols.y:
                #  Remember, col here is either a NUM or SYM object
                u.append(col.mid)

        elif cols == "x":
            for col in self.cols.x:
                #  Remember, col here is either a NUM or SYM object
                u.append(col.mid)

        elif cols == "all":
            for col in self.cols.all:
                #  Remember, col here is either a NUM or SYM object
                u.append(col.mid)

        else:
            #  This is our strange scenario where the str input in lets say an individual column
            for col in self.cols.all:
                if col.txt in cols:
                    #  Remember, col here is either a NUM or SYM object
                    u.append(col.mid)

        return Row(u)

    def div(self, cols):
        """
        Function returns the entropy/standard deviation of all or a selection of columns
        :param cols: A str that tells the function which columns to calculate on
        :return: Return an array that represents the sds/entropys of whatever columns were selected
        """
        u = []  # an array to be returned

        if cols == "y":
            for col in self.cols.y:
                #  Remember, col here is either a NUM or SYM object
                u.append(col.div)

        elif cols == "x":
            for col in self.cols.x:
                #  Remember, col here is either a NUM or SYM object
                u.append(col.div)

        elif cols == "all":
            for col in self.cols.all:
                #  Remember, col here is either a NUM or SYM object
                u.append(col.div)

        else:
            #  This is our strange scenario where the str input in lets say an individual column
            for col in self.cols.all:
                if col.txt in cols:
                    #  Remember, col here is either a NUM or SYM object
                    u.append(col.div)

        return Row(u)
