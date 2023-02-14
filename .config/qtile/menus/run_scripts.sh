#!/usr/bin/bash

scripts=(
    "record video"
    "record video & audio"
    "stop recording"
    "drop caches"
    "print selection"
    "print screen"
)

chosen_script=$(
    printf '%s\n' "${scripts[@]}" | rofi -dmenu -i -p "script:"
)

case $chosen_script in
    "record video")
        rec video;;
    "record video & audio")
        rec screencast;;
    "stop recording")
        rec kill;;
    "drop caches")
        sudo "$HOME/.local/bin/drop_caches";;
    "print selection")
        "$HOME/.local/bin/print" select;;
    "print screen")
        "$HOME/.local/bin/print" screen;;
esac

