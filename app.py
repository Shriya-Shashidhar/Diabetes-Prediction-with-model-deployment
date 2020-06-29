# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st


pickle_in=open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def Welcome():
    return "Welcome to Diabetes Prediction App"
    
# Creating a function for prediction
def predict_diabetes(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    """ Lets predict diabetes 
    This is the docstrings for specifications.
    ---
    parameters:
        - name: Pregnancies
          in: query
          type: number
          required: true
        - name: Glucose
          in: query
          type: number
          required: true
        - name: BloodPressure
          in: query
          type: number
          required: true
        - name: SkinThickness
          in: query
          type: number
          required: true
        - name: Insulin
          in: query
          type: number
          required: true
        - name: BMI
          in: query
          type: number
          required: true
        - name: DiabetesPedigreeFunction
          in: query
          type: number
          required: true
        - name: Age
          in: query
          type:  number
          required: true
    responses:
        200:
            description: The ouput values
    
    """

    prediction= classifier.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI,DiabetesPedigreeFunction,Age]])
    
    return "The answer is"+str(prediction)

def main():
    st.title("DIABETES PREDICTION")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Diabetes Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Pregnancies = st.text_input("Pregnancies","Type Here")
    Glucose = st.text_input("Glucose","Type Here")
    BloodPressure = st.text_input("PBloodPressure","Type Here")
    SkinThickness = st.text_input("SkinThickness","Type Here")
    Insulin = st.text_input("Insulin","Type Here")
    BMI = st.text_input("BMI","Type Here")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction","Type Here")
    Age = st.text_input("Age","Type Here")
    result = ""
    if st.button("Predict"):
        result= predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI,DiabetesPedigreeFunction,Age)
    st.success("The output is {}".format(result))
    if st.button("About"):
        st.text("App is built using streamlit")
        
        
if __name__=='__main__':
    main()
