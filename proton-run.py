#!/usr/bin/python3

import os
import requests

def get_steamid(game_name):
    url = f"https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(url)
    data = response.json()

    for app in data['applist']['apps']:
        if app['name'] == game_name:
            return app['appid']

    return None

executable = input("Which file would you like to run? ")
is_steam_game = input("Is this a steam game? (y/n) ")

if is_steam_game.lower() == "y":
    game_name = input("Enter the game name: ")
    steamid = get_steamid(game_name)
    if steamid is None:
        print(f"Could not find Steam ID for {game_name}")
        exit(1)
else:
    steamid = 480

os.environ["SteamAppId"] = str(steamid)
os.environ["STEAM_COMPAT_DATA_PATH"] = os.path.expanduser("~/proton/compatdata/")
os.environ["STEAM_COMPAT_CLIENT_INSTALL_PATH"] = os.path.expanduser("~/proton/GE-Proton8-13/proton")
os.system(f"waitforexitandrun {executable}")
