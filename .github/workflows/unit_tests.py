from main import get_prediction
import pytest


json = [
    {
        "id": "1",
        "gender": "Female",
        "age": 37,
        "hypertension": 1,
        "heart_disease": 1,
        "ever_married": "Yes",
        "work_type": "Private",
        "residence_type": "Urban",
        "avg_glucose_level": 228.69,
        "bmi": 36.6,
        "smoking_status": "formerly smoked"
    },
    {
        "id": "2",
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
    },
    {
        "id": "3",
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
]


def test_get_prediction_lr():
    prediction = get_prediction(model='lr', individuals=json, username='denis')
    assert prediction is not False


def test_get_prediction_rf():
    prediction = get_prediction(model='rf', individuals=json, username='hamid')
    assert prediction is not False





