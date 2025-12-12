import json
import requests

response = requests.get("http://api.github.com", timeout=10)
"""
print(f"Status Code: {response.status_code}")
print(f"Content-Type: {response.headers['Content-Type']}")
print(".text attributes:")
print(response.text)
print("\n")
print(".content attributes:")
print(response.text)
print("\n")
print(".json() method:")
print(response.content)
"""

# data = response.json()
# print("Available endpoints:")
# print(json.dumps(data, indent=2))

# for key in data.keys():
#     print(key)
    
response = requests.get(" https://github.com/swar/nba_api", timeout=10)

print(f"Status Code: {response.status_code}")

