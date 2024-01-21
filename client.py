
import json
import requests


host_url = "http://localhost:5005/model/parse"   #to determine the host port, refer to endpoint.yml

def nlu_respond(phrase: str) -> dict:
    nlu_data = json.dumps({'text': f"{phrase}"})
    nlu_resp = requests.post(host_url, data=nlu_data).json()
    return nlu_resp

print(nlu_respond("Hello, hows going?"))