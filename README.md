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
function test() {
  console.log("notice the blank line before this function?");
}
```

- POST ('/file_prediction') - get a prediction based on a source csv file. The function requires that one of the two models is passed as a parameter ('lr' - Logistic Regression or 'rf' - Random Forest Classifier).
<br />
The csv should contain the following columns:

| Name  | Data Type | Valid Values | 
| ------------- | ------------- | ------------- |
| id  | int  | |
| gender  | str  | |
| age  | float  | |
| hypertension  | int  | |
| heart_disease  | int  | |
| ever_married  | str  | |
| work_type  | str  | |
| residence_type  | str  | |
| avg_glucose_level  | float  | |
| bmi  | float  | |
| smoking_status | str | |


The following CURL can be used to test the endpoint:
```
function test() {
  console.log("notice the blank line before this function?");
}
```

## Deployment

A link to the Docker container can be found here: <https://hub.docker.com/example.com>

