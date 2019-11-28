import hashlib
import requests
import json

filename = input("Please enter the file path ")

hasher = hashlib.sha256()

with open(filename, 'rb') as open_file:
    content = open_file.read()
    hasher.update(content)

hash1 = hasher.hexdigest()
print (hasher.hexdigest())


url = 'https://www.virustotal.com/vtapi/v2/file/report'

params = {'apikey': '65b9735892e5b2fd75322240822780e975b9469cdbb745071e9cc3648e6fbef0', 'resource': hash1 }


response = requests.get(url, params=params)
data = json.loads(response.content.decode('utf-8'))
json_data = json.dumps(data, indent=2)

print (json_data)






