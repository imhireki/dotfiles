#!/usr/bin/bash

layouts=(
    "Monad"
    "Monad Focus"
    "Monad Wide"
    "Max"
    "Max Focus"
    "Floating"
)

chosen_layout=$(
    printf '%s\n' "${layouts[@]}" |\
    dmenu -i -c -l 6
)

utils="$XDG_CONFIG_HOME/qtile/custom/commands.py"

case $chosen_layout in
    Monad)
        python3 $utils change_to_layout 0 ;;
    "Monad Focus")
        python3 $utils change_to_layout 1 ;;
    "Monad Wide")
        python3 $utils change_to_layout 5 ;;
    Max)
        python3 $utils change_to_layout 2 ;;
    "Max Focus")
        python3 $utils change_to_layout 3 ;;
    "Floating")
        python3 $utils change_to_layout 4 ;;
esac

