import os
import requests
from requests.auth import HTTPBasicAuth

api_address = '172.29.1.1'
api_port = 8000

rf_model = 'rf'
lr_model = 'lr'
unknown_model = 'XX'
files = {'file': ('strokes_for_prediction.csv', open('strokes_for_prediction.csv', 'rb'), 'text/csv')}
files_txt = {'file': ('strokes_for_prediction.txt', open('strokes_for_prediction.txt', 'rb'), 'text/plain')}

# request1
def test_model_lr():
    r = requests.post(
        url='http://{address}:{port}/string_prediction?model={model}'.format(address=api_address, port=api_port, model=lr_model), auth=HTTPBasicAuth('denis', '12345'),
        headers={"Accept": "application/json"},
        json=[
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
    )

    output = '''
    ============================
        String prediction test
    ============================
    request done at "/string_prediction"
    | model="lr"
    expected result = [0, 1, 1]
    actual result = {result}
    ==>  {test_status}
    '''

    # Query status
    status_code = r.status_code
    # Query result
    result = r.json()

    # Display results
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(result=result, test_status=test_status))
    log = os.environ.get('LOG')
    # Printing in a file
    if os.environ.get('LOG') == '1':
        with open('./my_volume/api_test.txt', 'a') as file:
            file.write(output)


# request2
def test_model_rf():
    r = requests.post(
        url='http://{address}:{port}/string_prediction?model={model}'.format(address=api_address, port=api_port, model=rf_model), auth=HTTPBasicAuth('denis', '12345'),
        headers={"Accept": "application/json"},
        json=[
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
    )

    output = '''
    ============================
        String prediction test
    ============================
    request done at "/string_prediction"
    | model="rf"
    expected result = [0, 1, 1]
    actual result = {result}
    ==>  {test_status}
    '''

    # Query status
    status_code = r.status_code
    # Query result
    result = r.json()

    # Display results
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(result=result, test_status=test_status))

    # Printing in a file
    if os.environ.get('LOG') == '1':
        with open('./my_volume/api_test.txt', 'a') as file:
            file.write(output)


# request3
def test_model_unknown():
    r = requests.post(
        url='http://{address}:{port}/string_prediction?model={model}'.format(address=api_address, port=api_port, model=unknown_model), auth=HTTPBasicAuth('denis', '12345'),
        headers={"Accept": "application/json"},
        json=[
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
    )

    output = '''
    ============================
        String prediction test
    ============================
    request done at "/string_prediction"
    | model="unknown"
    expected result = Please select a valid model.
    actual result = {result}
    ==>  {test_status}
    '''

    # Query status
    status_code = r.status_code
    # Query result
    result = r.json()

    # Display results
    if status_code == 200 and result == 'Please select a valid model.':
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(result=result, test_status=test_status))

    # Printing in a file
    if os.environ.get('LOG') == '1':
        with open('./my_volume/api_test.txt', 'a') as file:
            file.write(output)

# request4
def test_file_lr():
    r = requests.post(
        url='http://{address}:{port}/file_prediction?model={model}'.format(address=api_address, port=api_port, model=lr_model), auth=HTTPBasicAuth('denis', '12345'),
        files=files
    )

    output = '''
    ============================
        File prediction test
    ============================
    request done at "/file_prediction"
    | model="lr"
    expected result = '[1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]'
    actual result = {result}
    ==>  {test_status}
    '''

    # Query status
    status_code = r.status_code
    # Query result
    result = r.json()

    # Display results
    if status_code == 200 and result["prediction"] == '[1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]':
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(result=result, test_status=test_status))

    # Printing in a file
    if os.environ.get('LOG') == '1':
        with open('./my_volume/api_test.txt', 'a') as file:
            file.write(output)

# request5
def test_file_rf():
    r = requests.post(
        url='http://{address}:{port}/file_prediction?model={model}'.format(address=api_address, port=api_port, model=rf_model), auth=HTTPBasicAuth('denis', '12345'),
        files=files
    )

    output = '''
    ============================
        File prediction test
    ============================
    request done at "/file_prediction"
    | model="rf"
    expected result = '[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]'
    actual result = {result}
    ==>  {test_status}
    '''

    # Query status
    status_code = r.status_code
    # Query result
    result = r.json()

    # Display results
    if status_code == 200 and result["prediction"] == '[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]':
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(result=result, test_status=test_status))

    # Printing in a file
    if os.environ.get('LOG') == '1':
        with open('./my_volume/api_test.txt', 'a') as file:
            file.write(output)

# request6
def test_file_unknown():
    r = requests.post(
        url='http://{address}:{port}/file_prediction?model={model}'.format(address=api_address, port=api_port, model=unknown_model), auth=HTTPBasicAuth('denis', '12345'),
        files=files
    )

    output = '''
    ============================
        File prediction test
    ============================
    request done at "/file_prediction"
    | model="unknown"
    expected result = 'Please select a valid model.'
    actual result = {result}
    ==>  {test_status}
    '''

    # Query status
    status_code = r.status_code
    # Query result
    result = r.json()

    # Display results
    if status_code == 200 and result == 'Please select a valid model.':
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(result=result, test_status=test_status))

    # Printing in a file
    if os.environ.get('LOG') == '1':
        with open('./my_volume/api_test.txt', 'a') as file:
            file.write(output)

# request7
def test_file_not_csv():
     r = requests.post(
         url='http://{address}:{port}/file_prediction?model={model}'.format(address=api_address, port=api_port,
                                                                            model=rf_model),
         auth=HTTPBasicAuth('denis', '12345'),
         files=files_txt
     )

     output = '''
     ============================
         File prediction test
     ============================
     request done at "/file_prediction"
     | model="rf"
     expected result = "{'detail': 'Invalid document type - please upload a CSV.'}"
     actual result = {result}
     ==>  {test_status}
     '''

     # Query status
     status_code = r.status_code
     # Query result
     result = r.json()
     print(result)

     # Display results
     if result == "{'Bad Type'}":
         test_status = 'SUCCESS'
     else:
         test_status = 'FAILURE'
     print(output.format(result=result, test_status=test_status))

     # Printing in a file
     if os.environ.get('LOG') == '1':
        with open('./my_volume/api_test.txt', 'a') as file:
            file.write(output)


##########################################################################################################################
test_model_lr()
test_model_rf()
test_model_unknown()
test_file_lr()
test_file_rf()
test_file_unknown()
#test_file_not_csv()
