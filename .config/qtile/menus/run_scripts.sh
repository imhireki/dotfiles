#!/usr/bin/bash

scripts=(
    "mpv"
    "magnet"
    "drop caches"
    "screenshot area"
    "screenshot screen"
    "record video"
    "record video & audio"
    "stop recording"
)

chosen_script=$(
    printf '%s\n' "${scripts[@]}" | rofi -dmenu -i -p "script"
)

case $chosen_script in
    "mpv") play_mpv &;;
    "magnet") magnet &;;
    "drop caches") sudo drop_caches &;;
    "screenshot area") screenshot area &;;
    "screenshot screen") screenshot screen &;;
    "record video") rec video &;;
    "record video & audio") rec screencast &;;
    "stop recording") rec kill &;;
esac

