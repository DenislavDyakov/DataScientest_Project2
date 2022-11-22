from data_preprocess import imput_missing_values, scale_values, encode_values, input_data, data_preprocessing
import pickle
import secrets
from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import List
import pandas as pd

import json

from schemas import Individual


app = FastAPI(
    title="API for Predicting Strokes",
    description="API for Predicting Strokes"
)


security = HTTPBasic()
users = {
    "denis": "12345",
    "hamid": "12345"
}


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = [True if credentials.username in users else False]

    if correct_username:
        correct_password = secrets.compare_digest(credentials.password, users[credentials.username])

    if correct_username is False or correct_password is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username



@app.get('/')
def landing_page():
    return {'hello': 'world'}


@app.post('/users/prediction', name='Get stroke prediction for one or more individuals')
async def get_prediction(model: str, individuals: List[Individual], username: str = Depends(get_current_username)):
    """Predict by using a list of 1 or more json objects as source data.\n
       The user should choose between 2 available models: \n
       lr - Logistic Regression \n
       rf - Random Forest Classifier \n
    """
    if model == "lr":
        choice = pickle.load(open('lr_best_classifier.pkl', 'rb'))
    elif model == "rf":
        choice = pickle.load(open('rf_best_classifier.pkl', 'rb'))
    else:
        return 'Please select a valid model.'

    patients = []
    for index, individual in enumerate(individuals):
        patient = {
            'id': individual.id,
            'gender': individual.gender,
            'age': individual.age,
            'hypertension': individual.hypertension,
            'heart_disease': individual.heart_disease,
            'ever_married': individual.ever_married,
            'work_type': individual.work_type,
            'residence_type': individual.residence_type,
            'avg_glucose_level': individual.avg_glucose_level,
            'bmi': individual.bmi,
            'smoking_status': individual.smoking_status
        }
        patients.append(patient)
    df = pd.DataFrame(patients)
    df = df.set_index('id')
    df = input_data(df)
    df = imput_missing_values(df)
    df = encode_values(df)
    df = scale_values(df)
    df = data_preprocessing(df)
    prediction = json.dumps(choice.predict(df).tolist())
    probability = json.dumps(choice.predict_proba(df).tolist())
    return {"user": username,
            "prediction": prediction,
            "probability": probability}


@app.post('/file/prediction', name='Get stroke prediction for individuals by using a file')
async def get_prediction_file(model: str, file: UploadFile = File(...), username: str = Depends(get_current_username)):
    """Predict by using a csv file as source data.\n
       The user should choose between 2 available models: \n
       lr - Logistic Regression \n
       rf - Random Forest Classifier \n
    """
    if model == "lr":
        choice = pickle.load(open('lr_best_classifier.pkl', 'rb'))
    elif model == "rf":
        choice = pickle.load(open('rf_best_classifier.pkl', 'rb'))
    else:
        return 'Please select a valid model.'

    df = pd.read_csv(file.filename, sep=',', header=0, index_col=0)
    df = input_data(df)
    df = imput_missing_values(df)
    df = encode_values(df)
    df = scale_values(df)
    df = data_preprocessing(df)
    prediction = json.dumps(choice.predict(df).tolist())
    probability = json.dumps(choice.predict_proba(df).tolist())
    return {"user": username,
            "prediction": prediction,
            "probability": probability}
