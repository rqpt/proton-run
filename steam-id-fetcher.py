#!/usr/bin/python3

import requests

def get_steamid(game_name):
    url = f"https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(url)
    data = response.json()
    
    for app in data['applist']['apps']:
        if app['name'] == game_name:
            return app['appid']
    
    return None

game_name = input("Enter the game name: ")
steamid = get_steamid(game_name)
print(steamid)
