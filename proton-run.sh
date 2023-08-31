#!/bin/bash

if [[ $1 ]]; then
  executable=$1
else
  echo "Which file would you like to run?"
  read executable
fi


if [[ -z $2 ]]; then

  while true; do
    echo "Is this a steam game? y/n"
    read -n 1 is_steam_game
    if [[ $is_steam_game == 'y' ]]; then
      echo ""
      id=$(steam-id-fetcher)
      echo ""
      break
    elif [[ $is_steam_game == 'n' ]]; then
      id=480
      break
    else
      echo ""
      echo "Only y/n answer, please"
      echo ""
    fi
  done

else
  id=$2
fi

SteamAppId=$id STEAM_COMPAT_DATA_PATH=$HOME/proton/compatdata/ STEAM_COMPAT_CLIENT_INSTALL_PATH=/ ~/proton/GE-Proton8-13/proton waitforexitandrun $executable
