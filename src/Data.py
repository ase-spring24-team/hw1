"""
File by Samuel Kwiatkowski-Martin
This file is our data class, which will contain and process columns and rows
"""
import random  # for our shuffling
from Row import Row  # Imports the Row class from the Row file
from util import csv  # Imports the csv function from util
from Cols import Cols  # Imports the Cols class


class Data:
    def __init__(self, src, func=None):
        """
        Initialization function for the data class
        Sets up rows and columns and calls to read in required values
        :param src: Either the csv filename or a list of rows
        :param func: An anonymous function, likely the function learn as of right now
        """
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            # checks if src is a string
            self.process_file(src, func)
        ## else the scenario where source is a table already
        else:
            self.add(src, func)
    def process_file(self, src, func=None):
        """
        Function that process the src file
        :param src: the csv file to be processed
        :param func: The anonymous function to continue being passed through
        :return: None
        """
        for row in csv(src):
            self.add(row, func)

    def add(self, t, func=None):
        """
        Function that adds rows and columns from the read csv
        :param t: t is the row to be added and should be passed as an array
        :param func: The anonymous function to be ran on each row before being added to a col
        :return: None
        """
        row = t if hasattr(t, 'cells') else Row(t)
        if self.cols is None:
            self.cols = Cols(row)
            # the following is not included in his lua code, but I believe we need it
            #self.rows.append((self.cols))
        else:
            if func is not None:
                # if the lambda function was passed to data
                func(self, row)
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
        u[".N"] = len(self.rows) - 1
        if cols == "y":
            if fun == "mid":
                for col in self.cols.y:
                    #  Remember, col here is either a NUM or SYM object
                    u[col.txt] = round(col.mid(), ndivs)
            elif fun == "div":
                for col in self.cols.y:
                    u[col.txt] = round(col.div(), ndivs)
            elif fun == "small":
                pass #  doesn't need to be implemented yet
        elif cols == "x":
            if fun == "mid":
                for col in self.cols.x:
                    #  Remember, col here is either a NUM or SYM object
                    u[col.txt] = round(col.mid(), ndivs)
            elif fun == "div":
                for col in self.cols.x:
                    u[col.txt] = round(col.div(), ndivs)
            elif fun == "small":
                pass #  doesn't need to be implemented yet
        elif cols == "all":
            if fun == "mid":
                for col in self.cols.all:
                    #  Remember, col here is either a NUM or SYM object
                    u[col.txt] = round(col.mid(), ndivs)
            elif fun == "div":
                for col in self.cols.all:
                    u[col.txt] = round(col.div(), ndivs)
            elif fun == "small":
                pass  # doesn't need to be implemented yet
        else:
            #  This is our strange scenario where the str input in lets say an individual column
            if fun == "mid":
                for col in self.cols.all:
                    if col.txt in cols:
                        #  Remember, col here is either a NUM or SYM object
                        u[col.txt] = round(col.mid(), ndivs)
            elif fun == "div":
                for col in self.cols.all:
                    if col.txt in cols:
                        u[col.txt] = round(col.div(), ndivs)
            elif fun == "small":
                pass  # doesn't need to be implemented yet
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

    def split(self, best, rest, lite, dark):
        selected = Data(self.cols.names)
        max = 1E30
        out = 1
        for (i, row) in enumerate(dark):
            b = row.like(best, len(lite), 2)
            r = row.like(rest, len(lite), 2)
            if b > r:
                selected.add(row)
            tmp = abs(b + r) / abs(b-r+1E-300)
            if tmp > max:
                out, max = i, tmp
        return out, selected
    
    def best_rest(self, rows, want):
        """
        This function divides the row as best and rest
        """
        rows = sorted(rows, key = lambda x : x.d2h(self))
        best = self.cols.names
        rest = self.cols.names
        for i, row in enumerate(rows):
            if i <= want:
                best.append(row)
            else:
                rest.append(row)
        return Data(best), Data(rest)

    def top_X(self, rows, top_num, option_num):
        """
        Prints the top X number of row's independent variable values
        :param rows: the shuffled rows object
        :param top_num: the total number of rows to have their y values printed
        :param option_num: just the num to be printedwws
        """
        i_var_indices = []  # list for the independent variable indices
        i_var_txts = []  # list of independent variable names
        for i_var in self.cols.y:
            # iterating over the different independent variables
            i_var_indices.append(i_var.at)
            i_var_txts.append(i_var.txt)
        print(f"{option_num}. top{top_num}", end=' ')
        for name in i_var_txts:
            print(f"{name},", end=' ')
        print()
        for i in range(top_num):
            print(f"Row {i + 1}", end=' ')
            for j in range(len(i_var_indices)):
                print(f"{rows[i][i_var_indices[j]]}", end=' ')
            print()
    def baseline3(self,closest_row):
        """
        This function prints the y values of the first row after sorting by d2h
        :param closest_row: The closest row to the heaven point
        """
        row = closest_row
        i_var_indices = []  # list for the independent variable indices
        i_var_txts = []  # list of independent variable names
        for i_var in self.cols.y:
            # iterating over the different independent variables
            i_var_indices.append(i_var.at)
            i_var_txts.append(i_var.txt)
        print(f"3. most ")
        for name in i_var_txts:
            print(f"{name},", end=' ')
        print()
        print(f"Row {1}", end=' ')
        for j in range(len(i_var_indices)):
            # print the y values of row
            print(f"{row[i_var_indices[j]]}", end=' ')
        print()

    def gate(self, budget0, budget, some):
        """
        This function guesses, accesses, transforms the data, and then evaluates
        :param budget0: initial number of rows to be evaluated
        :param budget: the number of rows to subsequently evaluate
        :param some: a constant float value to determine how many rows to place in best versus rest
        """
        stats = []
        bests = []
        rows = random.sample(self.rows, len(self.rows))  # shuffles rows
        top_X(rows, 6, 1)   # baseline #1
        top_X(rows, 50, 2)  # baseline #2

        # Now we must sort rows based on the distance to heaven -- will fix this once d2h is done
        rows.sort(key=lambda x: x.d2h(self))
        # print some stuff...
        baseline3(rows[0])  # baseline 3

        rows = random.sample(self.rows, len(self.rows))  # reshuffle rows
        lite = rows[0:budget0+1]  # grab first budget0 amount of rows
        dark = rows[budget0:]     # grab the remaining rows

        for i in range(budget):
            best, rest = best_rest(lite, len(lite)**some)   # sort our known rows into good vs bad
            todo, selected = split(best, rest, lite, dark)  # figuring out which row is the most
            # confusing --> todo will be the index of the MOST confusing value while selected
            # is a data object storing the rows from dark that most liked best(of which were tested)

            # ngl I'm not sure what the point of the following 2 lines is
            stats.append(selected.mid())
            bests.append(best.rows[0])

            # Insert into the lite, the most confusing example from dark(also remove the val from
            # dark
            lite.append(dark.pop(todo))
        return stats, bests

