import os
import requests
from requests.auth import HTTPBasicAuth

# Defibition of the API address
api_address = ''
# API port
api_port = 8000

# request1
def api_test1():
	r = requests.post(
    	url='http://{address}:{port}/users/prediction'.format(address=api_address, port=api_port), auth=HTTPBasicAuth('alice', 'wonderland'),
    	params= {
        	'model': 'rf'
    	},
    	json=[
        	{
        	"gender": 0,
        	"age": 40,
        	"hypertension": 1,
        	"heart_disease": 0,
        	"ever_married": 1,
        	"urban_residence": 0,
        	"avg_glucose_level": 90,
        	"bmi": 30,
        	"smoking_status": 0
        	},
       		{
        	"gender": 0,
        	"age": 60,
        	"hypertension": 1,
        	"heart_disease": 0,
        	"ever_married": 0,
        	"urban_residence": 0,
        	"avg_glucose_level": 150,
        	"bmi": 70,
        	"smoking_status": 1
        	},
        	{
        	"gender": 1,
        	"age": 33,
        	"hypertension": 1,
        	"heart_disease": 0,
        	"ever_married": 1,
        	"urban_residence": 0,
        	"avg_glucose_level": 200,
        	"bmi": 66,
        	"smoking_status": 1
        	}
    	]

  	)

	output = '''
	============================
    	Users prediction test
	============================
	request done at "/users/prediction"
	| model="rf"
	expected result = [0,1]
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

	log=os.environ.get('LOG')

	# Printing in a file
	if int(log) == 1:
	    with open('api_test.log', 'a') as file:
        	file.write(output)
