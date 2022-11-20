#!/bin/bash

reset_choices=(
    "All windows"
    "Main window"
    "Side windows"
)

chosen_reset=$(
    printf '%s\n' "${reset_choices[@]}" |\
    dmenu -i -c -l 3 
)

case $chosen_reset in
    "All windows") 
        qtile cmd-obj -o layout -f reset ;;
    "Main window")
        qtile cmd-obj -o layout -f normalize_main;;
    "Side windows")
        qtile cmd-obj -o layout -f normalize;;
esac

