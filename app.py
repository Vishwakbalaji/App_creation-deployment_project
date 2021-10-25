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
