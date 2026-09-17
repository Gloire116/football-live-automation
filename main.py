import os
import requests

API_KEY = os.environ.get("API_FOOTBALL_KEY")

if not API_KEY:
    raise Exception("La clé API_FOOTBALL_KEY est introuvable.")

url = "https://v3.football.api-sports.io/fixtures?live=all"

headers = {
    "x-apisports-key": API_KEY
}

response = requests.get(url, headers=headers, timeout=30)

print("Code HTTP :", response.status_code)

data = response.json()

print("Nombre de matchs :", data.get("results", 0))

if data.get("errors"):
    print("Erreurs API :", data["errors"])

for match in data.get("response", []):
    home = match["teams"]["home"]["name"]
    away = match["teams"]["away"]["name"]

    home_score = match["goals"]["home"]
    away_score = match["goals"]["away"]

    minute = match["fixture"]["status"]["elapsed"]

    print(f"{home} {home_score} - {away_score} {away} | {minute}'")
