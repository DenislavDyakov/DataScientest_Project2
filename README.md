# DataScientest_Project2

## Introduction
This repository contains the files for the second project of the Data Engineering program of DataScientest. 
<br />
The goal of this project is to build a RESTful API, which serves to deploy a machine learning model for predicting whether a person might have a stroke. 
<br />
## Structure
The diagram below provides an overview of the current functionalities.
<img src="https://user-images.githubusercontent.com/8698545/203444336-83237e75-121b-4105-8a95-47835e8551de.jpg" width="600">
<br /><br />

The repo consists of the following folders:
- Model - contains the pickle files for the two ML models, which provided the highest F-scores.
- API - python scripts of the main API files
- Docker - the Docker files and docker-compose file for deploying and testing the APIs
<br />

## Endpoints

- GET ('/') - landing page

- POST ('/string_prediction') - get a prediction based on a source json string. The function requires that one of the two models is passed as a parameter ('lr' - Logistic Regression or 'rf' - Random Forest Classifier)

The follwoing CURl can be used to test the endpoint:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/string_prediction?model=lr' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
  {
    "id": "11111",
    "gender": "Male",
    "age": 67,
    "hypertension": 1,
    "heart_disease": 1,
    "ever_married": "Yes",
    "work_type": "Private",
    "residence_type": "Urban",
    "avg_glucose_level": 228.69,
    "bmi": 36.6,
    "smoking_status": "formerly smoked"
  }
]'
```

- POST ('/file_prediction') - get a prediction based on a source csv file. The function requires that one of the two models is passed as a parameter ('lr' - Logistic Regression or 'rf' - Random Forest Classifier).
<br />
The csv should contain the following columns:

| Name  | Data Type | Valid Values | 
| ------------- | ------------- | ------------- |
| id  | int  | any integer value|
| gender  | str  | 'Male', 'Female'|
| age  | float  | any integer value|
| hypertension  | int  | any integer value|
| heart_disease  | int  | 0 or 1|
| ever_married  | str  | 'Yes', 'No'|
| work_type  | str  | 'Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked' |
| residence_type  | str  | 'Urban', 'Rural'|
| avg_glucose_level  | float  | any float value|
| bmi  | float  | any float value|
| smoking_status | str | 'formerly smoked', 'never smoked', 'smokes', 'Unknown'|


The following CURL can be used to test the endpoint:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/file_prediction?model=lr' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@strokes_for_prediction.csv;type=text/csv'
```

## Deployment

A link to the Docker container can be found here: <https://hub.docker.com/repository/docker/younesabdh/stroke_api_image>

