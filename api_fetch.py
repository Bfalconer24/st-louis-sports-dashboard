import requests

url = "https://www.thesportsdb.com/api/v1/json/123/lookup_all_players.php?id=133604"

response = requests.get(url)

data = response.json()

print(data.keys())