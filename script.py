import requests

url = "http://localhost:9000/predict"
data = {
    "age": 30,
    "bmi": 25.0,
    "children": 1,
    "sex": "male",
    "smoker": "no",
    "region": "northeast"
}

response = requests.post(url, json=data)
print(response.json())  