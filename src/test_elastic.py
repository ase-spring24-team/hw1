"""
File created by Samuel Kwiatkowski-Martin
This class represents
"""
import csv
import re
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
    amount_of_x_values = len(data.cols.x)
    amount_of_y_values = len(data.cols.y)
    X = []  # will be our X list for inputs to our Elastic net
    Y = []
    counter = 0
    max = len(data.rows)/2
    for row in data.rows:
        if counter > max:
            break  # break out of the loop if we have trained the model on half the data
        x = row.cells[:amount_of_x_values]
        if "?" not in x:
            #  If we are missing a value in our x input, that will break our model
            X.append(x)
            Y.append(row.cells[-amount_of_y_values:])
        counter += 1
    X = np.array(X)
    Y = np.array(Y)

    # For creating and writing the csv file with a good naming convention
    reg = r'[^./]*(?=\.[^./]*$)'
    data_name = re.search(reg, data_file).group(0)
    file_path = f'../data/{data_name}_elasticnet_hyperparameters.csv'

    # Writing to CSV
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['alpha', 'l1_ratio', 'fit_intercept', 'max_iter', 'selection', 'warm_start', 'tol', 'error-'])
        alpha = .1
        while alpha <= 10:
            l1_ratio = 0
            while l1_ratio <= 1:
                for fit_intercept in [True, False]:
                    for max_iter in range(300, 5000, 500):
                        for selection in ['cyclic', 'random']:
                            for warm_start in [True, False]:
                                tol = .00000001
                                while tol <= .1:
                                    regr = ElasticNet(random_state=0, alpha=alpha,
                                                      l1_ratio=l1_ratio,
                                                      fit_intercept=fit_intercept,
                                                      max_iter=max_iter, selection=selection,
                                                      warm_start=warm_start, tol=tol)
                                    regr.fit(X, Y)
                                    prediction_data_point = np.array(
                                        [data.rows[-1].cells[:amount_of_x_values]])
                                    prediction2 = regr.predict(prediction_data_point)
                                    actual = np.array(data.rows[-1].cells[-amount_of_y_values:])
                                    error = actual - prediction2
                                    error = abs(error / actual)
                                    error = np.linalg.norm(error - np.array([0, 0, 0]))
                                    print(f"Elastic Net {prediction2}. Error {error}")
                                    writer.writerow([alpha, l1_ratio, fit_intercept, max_iter, selection, warm_start, tol, error])
                                    tol *= 10

                l1_ratio += .1
            alpha += .1
    """
    regr = ElasticNet(random_state=0)
    regr.fit(X, Y)
    prediction_data_point = np.array([data.rows[-1].cells[:amount_of_x_values]])
    prediction2 = regr.predict(prediction_data_point)
    print(prediction2[0])
    actual = np.array(data.rows[-1].cells[-amount_of_y_values:])
    error = actual - prediction2
    error = abs(error/actual)
    print(error)
    error = np.linalg.norm(error-np.array([0,0,0]))
    print(f"Elastic Net {prediction2}")
    print(f"Real Answer {actual}")
    print(f"Error: {error}")
    """

if __name__ == '__main__':
    the._set(SLOTS({"file":"../data/auto93.csv", "__help": "", "m":2, "k":1, "p":2, "Half":256, "d":32, "D":4,
                    "Far":.95, "seed":31210, "Beam":10, "bins":16, "Cut":.1, "Support":2}))

    #call the function we want to run here
    create_elastic_data_set("../data/auto93.csv")
