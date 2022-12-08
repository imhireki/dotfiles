#!/bin/bash

apps=(
    "Terminal"
    "Web Browser"
    "Text Editor"
    "Notebook"
    "File Manager"
    "Music Player"
    "Torrent Downloader"
)

chosen_app=$(printf '%s\n' "${apps[@]}" | dmenu -i -c -l 8)

case $chosen_app in
    "Terminal")
        alacritty;;
    "Web Browser")
        qutebrowser;;
    "Text Editor")
        alacritty --class neovim -e nvim;;
    "Notebook")
        alacritty --class notebook -e nvim ~/notes/agenda.org;;
    "File Manager")
        alacritty --class ranger -e ranger;;
    "Music Player")
        if ! [pgrep mpd]; then mpd; fi
        alacritty --class ncmpcpp -e ncmpcpp;;
    "Torrent Downloader")
        if ! [pgrep transmission-daemon]; then
            transmission-daemon
        fi
        alacritty --class stig -e stig;;
esac

