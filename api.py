from fastapi import FastAPI, Depends, Header, HTTPException, status, File, UploadFile
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List
import pandas as pd
import numpy as np
import json
from random import choices
from sklearn import metrics
from sklearn.model_selection import train_test_split
import joblib
from joblib import dump, load
import pickle

users = {
  "alice": "wonderland",
  "bob": "builder",
  "clementine": "mandarine"
}

#lr_model=pickle.load(open('lr_best_classifier.pkl','rb'))
#rf_model=pickle.load(open('rf_best_classifier.pkl','rb'))


class Individual(BaseModel):
    gender: int
    age: float
    hypertension: int
    heart_disease: int
    ever_married: int
    urban_residence: int
    avg_glucose_level: float
    bmi: float
    smoking_status: int
        
api = FastAPI(
    title="Model API",
    description="API to predict if a person will have a stroke or not",
    version="1.0.0",
    openapi_tags=[
    {
        'name': 'Home',
        'description': 'Default functions'
    },
    {
        'name': 'Performance',
        'description': 'Functions that are used to deal with performances'
    },
    {
        'name': 'Prediction',
        'description': 'Functions that are used to deal with predictions'
    }
    ]
)

security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    for key, value in users.items():
        if credentials.username==key and credentials.password==value:
            return credentials.username

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password",
        headers={"WWW-Authenticate": "Basic"},
    )

def get_admin_username(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username=='admin' and credentials.password=='4dm1N':
        return credentials.username

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password",
        headers={"WWW-Authenticate": "Basic"},
    )

    
@api.get('/status', name='Get API status', tags=['Home'])
def get_status(username: str = Depends(get_current_username)):
    return " API is working"


@api.post('/users/prediction', name='Get stroke prediction for one or more individuals', tags=['Prediction'])
async def get_prediction(model: str, individuals: List[Individual], username: str = Depends(get_current_username)):
    """This function returns stroke predictions for ine or many individuals.\n
       MODEL : lr (LogisticRegression) / rf (Random Forest Classification)
    """
    
    try:
        if (model=="lr"):
            choice = lr_model
            name = 'LogisticRegression'
        elif (model=="rf"):
            choice = rf_model
            name = 'RandomForestClassifier'
        else: 
            return 'The given model is missing or incorrect'

        individus = []
        for index, individual in enumerate(individuals):
            individu = {
                'id': index,
                'gender': individual.gender,
                'age': individual.age,
                'hypertension': individual.hypertension,
                'heart_disease': individual.heart_disease,
                'ever_married': individual.ever_married,
                'urban_residence': individual.urban_residence,
                'avg_glucose_level': individual.avg_glucose_level,
                'bmi': individual.bmi,
                'smoking_status': individual.smoking_status
            }
            individus.append(individu)
        df = pd.DataFrame(individus)
        df = df.set_index('id')
        scaler=load('../Model/minmax_scaler.bin')
        df = scaler.transform(df)
        pred =choice.predict(df)
        pred_lists = pred.tolist()
        pred_jason = json.dumps(pred_lists)
        return pred_jason

    except IndexError:
        raise HTTPException(
            status_code=404,
            detail='Unknown Index')
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail='Bad Type'
        )

@api.post('/file/prediction', name='Get stroke prediction for individuals by using a file', tags=['Prediction'])
async def get_prediction_file(model: str, csv_file: UploadFile = File(...), username: str = Depends(get_current_username)):
    """This function returns stroke prediction for individuals by using a file.\n
       MODEL : lr (LogisticRegression) / rf (Random Forest Classification)
    """
    
    try:
        if (model=="lr"):
            choice = lr_model
            name = 'LogisticRegression'
        elif (model=="rf"):
            choice = rf_model
            name = 'RandomForestClassifier'
        else: 
            return 'The given model is missing or incorrect'
            
        df = pd.read_csv(csv_file.file, sep = ',', header = 0, index_col = 0)
        scaler=load('../Model/minmax_scaler.bin')
        df = scaler.transform(df)
        pred = choice.predict(df)
        pred_lists = pred.tolist()
        pred_jason = json.dumps(pred_lists)
        return pred_jason
            
    except IndexError:
        raise HTTPException(
            status_code=404,
            detail='Unknown Index')
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail='Bad Type'
        )
