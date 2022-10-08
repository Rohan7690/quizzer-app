import requests
parameters = {
    "amount": 10,
    "type": "boolean"
    }
api = requests.get("https://opentdb.com/api.php",params=parameters)
api.raise_for_status()
data = api.json()
question_data = data["results"]
