import requests
import json

IP = input("Please enter the IP address: ")

URL1 = str("http://api.ipstack.com/") + IP + str("?access_key=a0ce87365de4d1b0659f1511d2d9a397")


response = requests.get(URL1)
data = json.loads(response.content.decode('utf-8'))
json_data = json.dumps(data, indent=2)

print (json_data)

