# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 10:58:37 2021

@author: Khobeib
"""

import pandas as pd
import pickle
import numpy as np
import streamlit as st
with open('r"/app/musicPredictor.pkl','rb') as f:
    mymodel = pickle.load(f)
    

def myPredictor(age, gender):
    ageInput = age
    genderInput = gender
    prediction = mymodel.predict([[ageInput,genderInput]])
    return "The prediction is: " + str(prediction)

def main():
    st.title("Music Predictor")
    theAge = st.text_input("Age:","Type your age")
    theGender = st.text_input("Gender:","Type your gender e.g. M or F")
    genderValue = 4
    if ((theGender =="M") | (theGender == "m")):
        genderValue = 1
    elif ((theGender =="F") | (theGender == "f")):
        genderValue = 0
    else:
        genderValue = 4
        
    theResult = ""
    if st.button("Predict"):
        theResult = myPredictor(theAge, genderValue)
    
    st.success("Output: {}".format(theResult))
    
if __name__ == "__main__":
    main()
