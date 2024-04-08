"""
File created by Samuel Kwiatkowski-Martin
This class represents
"""
import csv
import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import LinearRegression
from the import THE, the, SLOTS
from Data import Data

# First we must write an algorithm that can create a data set which represents all the possible
# sets of hyperparameters and their outputs based on inputing the last row of the input data set
# for example with auto93, we will train on the first half of the data, and we will test all the
# different hyperparameters and what the Elastic net outputs given that the input was instead the
# last row from auto93 -> long term I am thinking we need to train on the first half of the data
# and then predict on the remaining half, but let's just start small


def create_elastic_data_set(data_file):
    """
    This function creates a data csv similar to auto93 except that the X values are hyperparameters
    and the y values are the predicted y values based on the input row (car in auto93)
    """
    data = Data(data_file)  # creates the data object
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
    # y = 1 * x_0 + 2 * x_1 + 3
    y1, y2 = np.dot(X, np.array([1, 2])) + 3, np.dot(X, np.array([1, 2]))
    print(y1)
    y = np.concatenate((y1[:, np.newaxis], y2[:, np.newaxis]),
                       axis=1)  # Concatenate y1 and y2 to form a 2D array
    print(y.shape)
    print(y)
    regr = ElasticNet(random_state=0)
    regr.fit(X, y)
    prediction2 = regr.predict(np.array([[3, 5]]))
    reg = LinearRegression(fit_intercept=True, positive=False).fit(X, y)
    reg.score(X, y)
    reg.coef_
    reg.intercept_
    prediction = reg.predict(np.array([[3, 5]]))
    print(f"Normal Linear Regression {prediction}")
    print(f"Elastic Net {prediction2}")
    print(f"Real Answer {16}")

if __name__ == '__main__':
    the._set(SLOTS({"file":"../data/auto93.csv", "__help": "", "m":2, "k":1, "p":2, "Half":256, "d":32, "D":4,
                    "Far":.95, "seed":31210, "Beam":10, "bins":16, "Cut":.1, "Support":2}))

    #call the function we want to run here
    create_elastic_data_set("../data/auto93.csv")
