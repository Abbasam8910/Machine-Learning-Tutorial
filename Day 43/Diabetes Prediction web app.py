import numpy as np
import pandas as pd
import pickle
import streamlit as st

# Loading the saved model

loaded_model = pickle.load(open('d:/# My Learning/Coding/Machine-Learning-Tutorial/Day 43/trained_model.sav', 'rb'))


def diabates_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return'The person is diabetic'


def main():
    
    # Giving a title 
    st.title('Diabetes Prediction')

    # Getting the input from user

    Pregnancies = st.text_input('No of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    Skinthickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    Body_mass_index = st.text_input('BMI Value')
    Diabetespedgreefunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input("Age of the Person")

    # code for prediction

    diagnosis = ''

    # creating a button for prediction

    if st.button('Diabetes Test Result'):
        diagnosis = diabates_prediction([Pregnancies, Glucose, BloodPressure, Skinthickness, Insulin, Body_mass_index, Diabetespedgreefunction, Age])


    st.success(diagnosis)


if __name__=='__main__':
    main()