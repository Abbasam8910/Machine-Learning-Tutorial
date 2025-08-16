import pandas as pd
import numpy as np
class Logistic_Regression():

    # Initiating the Paramerters (Learning Rate and No of Iteration)

    def __init__(self, learning_rate, no_of_iteration):

        self.learning_rate = learning_rate
        self.no_of_iteration = no_of_iteration

    def fit(self, X, Y):

        # No of Training Examples and No of Features

        # number of data points in the dataset (number of rows)  -->  m
        # number of input features in the dataset (number of columns)  --> n

        self.m, self.n = X.shape    

        #Initiating The Weights and Bias

        self.w = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.Y = Y

        # Implementing Gradient Descent

        for i in range(self.no_of_iteration):
            self.Update_Weight()


    def Update_Weight(self):

        # Y_hat Formula (Sigmoid Function)

        Z = self.X.dot(self.w) + self.b
        Y_hat =  (1 / (1 + np.exp(-Z)))

        # Derivative

        dw = (1 / self.m) * np.dot(self.X.T, (Y_hat - self.Y))
        db = (1 / self.m) * np.sum(Y_hat - self.Y)

        # Update Weight and Bias Using Gradient Descent

        self.w = self.w - self.learning_rate * dw
        self.b = self.b - self.learning_rate * db

    # Sigmoid Equation and Decision Boundary

    def Predict(self, X):
        Z = X.dot(self.w) + self.b
        Y_pred =  (1 / (1 + np.exp(-Z)))
        Y_pred = np.where(Y_pred > 0.5, 1, 0)
        return Y_pred
