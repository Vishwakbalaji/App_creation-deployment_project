import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

import os
os.chdir(r'C:\Users\Yogesh\python learn\Praxis\DMD')
pickle_in = open('pickle_file_car.pkl',"rb")
classifier=pickle.load(pickle_in)

def mpg_predictor(Cylinders,Horsepower,Weight,Acceleration):

    """Trying to predict MPG using certian parameter
    This is using docstrings for specifications.
    ---
    parameters:
      - name: Cylinders
        in: query
        type: number
        required: true
      - name: Horsepower
        in: query
        type: number
        required: true
      - name: Weight
        in: query
        type: number
        required: true
      - name: Acceleration
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """

    prediction=classifier.predict([[Cylinders,Horsepower,Weight,Acceleration]])
    print(prediction)
    return prediction

def main():
    #st.title("Car MPG Predictor" , )
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> Car MPG Predictor Web App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    Cylinders = st.text_input("Cylinders","Type Here number of Cylinders (8, 4, 6, 3, 5)")
    Horsepower = st.text_input("Horsepower","Type Here Horsepower range between (0-250)")
    Weight = st.text_input("Weight","Type Here Weight range between (600-6000)")
    Acceleration = st.text_input("Acceleration","Type Here Horsepower range between (8-25)")
    result=""
    if st.button("Predict"):
        result=mpg_predictor((Cylinders),(Horsepower),(Weight),(Acceleration))
        result = np.round(result)[0]
        result = result[0]
    st.success('The predicted Car MPG is {}'.format(result))
    if st.button("About"):
        st.text("This apps help to predict Car's MPG")
        st.text("Built with Streamlit")

os.chdir(r'C:\Users\Yogesh\python learn\krish')

if __name__=='__main__':
    main()
