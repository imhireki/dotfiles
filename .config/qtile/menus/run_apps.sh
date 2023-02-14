#!/usr/bin/bash

apps=(
    "terminal"
    "web browser"
    "text editor"
    "notebook"
    "file manager"
    "music player"
    "torrent downloader"
    "document reader"
    "audio controller"
)

chosen_app=$(printf '%s\n' "${apps[@]}" | rofi -dmenu -i -p "app:")

case $chosen_app in
    "terminal")
        alacritty;;
    "web browser")
        qutebrowser;;
    "text editor")
        alacritty --class neovim -e nvim;;
    "notebook")
        notebook=$(/bin/ls "$HOME/notes" | rofi -dmenu -i -p "notebook: ")
        alacritty --class notebook -e nvim "$HOME/notes/$notebook";;
    "file manager")
        alacritty --class ranger -e ranger;;
    "music player")
        if ! [pgrep mpd]; then mpd; fi
        alacritty --class ncmpcpp -e ncmpcpp;;
    "torrent downloader")
        if ! [pgrep transmission-daemon]; then
            transmission-daemon
        fi
        alacritty --class stig -e stig;;
    "document reader")
      zathura;;
    "audio controller")
      alacritty --class pulsemixer -e pulsemixer;;
esac

