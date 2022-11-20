#!/bin/bash

apps=(
    "Alacritty"
    "Qutebrowser"
    "Discord"
    "Emacs"
    "Ranger"
    "Ncmpcpp"
    "Neovim"
    "Stig"
)

chosen_app=$(printf '%s\n' "${apps[@]}" | dmenu -i -c -l 8)

case $chosen_app in
    Alacritty)
        alacritty;;
    Qutebrowser)
        qutebrowser;;
    Discord)
        discord;;
    Emacs)
        emacsclient -c -a "emacs";;
    Ranger)
        alacritty --class ranger -e ranger;;
    Ncmpcpp)
        if ! [pgrep mpd]; then mpd; fi
        alacritty --class ncmpcpp -e ncmpcpp;;
    Stig)
        if ! [pgrep transmission-daemon]; then
            transmission-daemon
        fi
        alacritty --class stig -e stig;;
    Neovim)
        alacritty --class neovim -e nvim;;
esac


