#!/bin/bash

session_controls=(
    "Restart Qtile"
    "Shutdown Qtile"
    "Poweroff"
    "Reboot"
    "Suspend"
)

chosen_session_control=$(
    printf '%s\n' "${session_controls[@]}" |\
    dmenu -i -c -l 5
)

case $chosen_session_control in
    "Restart Qtile")
        qtile cmd-obj -o cmd -f restart;;
    "Shutdown Qtile")
        qtile cmd-obj -o cmd -f shutdown;;
    Poweroff)
        loginctl poweroff;;
    Reboot)
        loginctl reboot;;
    Suspend)
        sudo "$HOME/.local/bin/susp";;
esac

