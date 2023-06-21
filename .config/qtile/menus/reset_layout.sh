#!/usr/bin/bash

reset_choices=(
    "all windows"
    "main window"
    "side windows"
)

chosen_reset=$(
    printf '%s\n' "${reset_choices[@]}" |\
    rofi -dmenu -i -p "layout reset"
)

case $chosen_reset in
    "all windows") 
        qtile cmd-obj -o layout -f reset ;;
    "main window")
        qtile cmd-obj -o layout -f normalize_main;;
    "side windows")
        qtile cmd-obj -o layout -f normalize;;
esac

