#!/usr/bin/python3

import os
import requests
import sys

def get_steamid(game_name):
    url = f"https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(url)
    data = response.json()

    for app in data['applist']['apps']:
        if app['name'] == game_name:
            return app['appid']

    return None

executable = sys.argv[1]
is_steam_game = input("Is this a steam game? (y/n) ")

if is_steam_game.lower() == "y":
    game_name = input("Enter the game name: ")
    steamid = get_steamid(game_name)
    print(f"The SteamId for this game is {steamid}")
    if steamid is None:
        print(f"Could not find Steam ID for {game_name}")
        exit(1)
else:
    steamid = 480

os.system(f"SteamAppId={steamid} STEAM_COMPAT_DATA_PATH=~/proton/compatdata/ STEAM_COMPAT_CLIENT_INSTALL_PATH=/ ~/proton/GE-Proton8-13/proton waitforexitandrun {executable}")
