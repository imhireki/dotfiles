#!/bin/bash

scripts=(
    "Record video"
    "Record video & audio"
    "Stop recording"
    "Drop caches"
    "Print selection"
    "Print screen"
)

chosen_script=$(
    printf '%s\n' "${scripts[@]}" | dmenu -i -c -l 6
)

case $chosen_script in
    "Record video")
        rec video;;
    "Record video & audio")
        rec screencast;;
    "Stop recording")
        rec kill;;
    "Drop caches")
        sudo "$HOME/.local/bin/drop_caches";;
    "Print selection")
        "$HOME/.local/bin/print" select;;
    "Print screen")
        "$HOME/.local/bin/print" screen;;
esac

