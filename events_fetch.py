import requests

url = url = "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Arsenal_vs_Chelsea"
response = requests.get(url)
data = response.json()

print(data)