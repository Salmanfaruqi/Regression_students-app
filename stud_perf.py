import streamlit as st
import pandas as pd
import numpy as np
import pickle
# from sklearn.preprocessing import StandardScaler

def load_model():
    with open("linear_regression_model.pkl", 'rb') as file:
        model, scaler, le =  pickle.load(file)
    return model, scaler, le

def preprocessing_input_data(data, scaler, le):
    data['Extracurricular Activities'] = le.transform([data['Extracurricular Activities']])[0]
    df = pd.DataFrame([data])
    df_transformed =  scaler.transform(df)
    return df_transformed


def predict_data(data):
    model, scaler, le = load_model()
    preprocessed_data = preprocessing_input_data(data, scaler, le)
    prediction = model.predict(preprocessed_data)
    return prediction[0]


def main(): 
    st.title("Student Prediction")
    st.write("Enter your detail to get prediction on your input")

    hour_studied = st.number_input("Hours Studied", min_value=1, max_value=10, value=5)
    previous_scores = st.number_input("Previous Scores", min_value=40, max_value=100, value=70)
    Extracurricular_Activities = st.selectbox("Extracurricular Activities",["Yes", "No"])
    sleep_hours = st.number_input("Sleep Hours", min_value=4, max_value=10, value=7)
    Question_Papers = st.number_input("Question Paper", min_value=0, max_value=10, value=5)

    if st.button("Predict your Score"):
        user_data = {
            "Hours Studied": hour_studied,
            "Previous Scores":  previous_scores,
            "Extracurricular Activities": Extracurricular_Activities,
            "Sleep Hours": sleep_hours,
            "Sample Question Papers Practiced": Question_Papers
        }
        prediction = predict_data(user_data)
        st.success(f"Prediction Result is: {prediction}")

if __name__ == "__main__":
    main()










