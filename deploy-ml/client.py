import requests
body = {
    "age": 54,
    "sex": 0,
    "cp": 3,
    "trestbps": 120,
    "chol": 167,
    "fbs": 0,
    "restecg": 0,
    "thalach": 99,
    "exang": 1,
    "oldpeak": 1.8,
    "slope": 1,
    "ca": 2,
    "thal": 2
    }
response = requests.post(url = 'http://127.0.0.1:8000/score',
              json = body)
print (response.json())
# output: {'score': 0.866490130600765}