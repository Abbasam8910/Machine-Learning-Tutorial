import numpy as np
class Linear_Regression():

# Initiating the Paramerters (Learning Rate and No of Iteration)

    def __init__(self, learning_rate, no_of_iterations):

        self.learning_rate = learning_rate
        self.no_of_iterations = no_of_iterations
    
    def fit(self, X, Y):

        # No of training examples and no of features

        self.m, self.n = X.shape  # No of rows and cols

        # Initiating the weight and bias
        self.w = np.zeros(self.n) 
        self.b = 0
        self.X = X
        self.Y = Y

        # Implementing Gradient Descent

        for i in range(self.no_of_iterations):
            self.Update_Weight()



    def Update_Weight(self):

        Y_prediction = self.Predict(self.X)

        # Calculate Gradient

        dw = -(2 * (self.X.T).dot(self.Y - Y_prediction))/self.m
        db = -2 * np.sum(self.Y - Y_prediction)/ self.m

        # Update weights

        self.w = self.w - self.learning_rate * dw
        self.b = self.b - self.learning_rate * db


    def Predict(self, X):

        return X.dot(self.w) + self.b

