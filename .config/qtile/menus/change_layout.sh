#!/usr/bin/bash

layouts=(
    "monad"
    "monad focus"
    "monad wide"
    "monad wide focus"
    "max"
    "max focus"
    "floating"
    "floating focus"
)

chosen_layout=$(
    printf '%s\n' "${layouts[@]}" |\
    rofi -dmenu -i -p "windows layout"
)

utils="$XDG_CONFIG_HOME/qtile/custom/commands.py"

case $chosen_layout in
    monad)
        python3 $utils change_to_layout 0 ;;
    "monad focus")
        python3 $utils change_to_layout 1 ;;
    "monad wide")
        python3 $utils change_to_layout 2 ;;
    "monad wide focus")
        python3 $utils change_to_layout 3 ;;
    max)
        python3 $utils change_to_layout 4 ;;
    "max focus")
        python3 $utils change_to_layout 5 ;;
    "floating")
        python3 $utils change_to_layout 6 ;;
    "floating focus")
        python3 $utils change_to_layout 7 ;;
esac

