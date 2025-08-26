import numpy as np
class SVM_Classifier():

    # Initiating The Hyperparameters

    def __init__(self, learning_rate, no_of_iteration, lambda_parameter):

        self.learning_rate = learning_rate
        self.no_of_iteration = no_of_iteration
        self.lambda_parameter = lambda_parameter

    # Fitting the dataset to SVM Classifer

    def fit(self, X, Y):

        # m -> no of data points ( no of rows)
        # n -> no of input features (no of cols)

        self.m, self.n = X.shape

        # Initiating the weight value and bias value

        self.w = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.Y = Y

        # Implementing Gradient Descent Algorithm for Optimization

        for i in range(self.no_of_iteration):
            self.update_weight()


    # Function for updating weight and bias value

    def update_weight(self):

        # Label Encoding
        y_label = np.where(self.Y <=0, -1, 1)


    # Gradients (dw,db)

        for index, x_i in enumerate(self.X):
            condition = y_label[index] * (np.dot(x_i, self.w) - self.b) >=1

            if (condition == True):

                dw = 2 * self.lambda_parameter * self.w
                db = 0

            else:

                dw = 2 * self.lambda_parameter * self.w - np.dot(x_i, y_label[index])
                db = y_label[index]


            self.w = self.w - self.learning_rate * dw
            self.b = self.b - self.learning_rate * db


    # Predict the label for the given input

    def predict(self, X):
        output = np.dot(X, self.w) - self.b

        predicted_labels = np.sign(output)

        y_hat = np.where(predicted_labels <=-1, 0, 1)

        return y_hat

