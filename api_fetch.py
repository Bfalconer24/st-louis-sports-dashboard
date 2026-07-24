import requests

print("Sports Dashboard Started")

url = "https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t=Argentina" 

print(url)

response = requests.get(url)
print(response.status_code)

data = response.json()

print(data)

if data["teams"] is None:
    print("No teams found.")
else:
    for team in data["teams"]:
        print(team["strTeam"])
        print(team["strLeague"])
        print(team["strStadium"])
        print(team["strCountry"])
        print(team["intFormedYear"])