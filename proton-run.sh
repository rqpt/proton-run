#!/bin/bash

if [[ $1 ]]; then
  executable=$1
else
  echo "Which file would you like to run?"
  read executable
fi

if [[ $2 ]]; then
  SteamAppId=480
else
  echo "Please provide the SteamAppId for the game: "
  read SteamAppId
fi

STEAM_COMPAT_DATA_PATH=$HOME/proton/compatdata/
STEAM_COMPAT_CLIENT_INSTALL_PATH=/
~/proton/GE-Proton8-13/proton waitforexitandrun executable
