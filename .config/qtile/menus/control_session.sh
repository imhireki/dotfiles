#!/usr/bin/bash

session_controls=(
    "restart qtile"
    "shutdown qtile"
    "poweroff"
    "reboot"
    "suspend"
)

chosen_session_control=$(
    printf '%s\n' "${session_controls[@]}" |\
    rofi -dmenu -i -p "session"
)

case $chosen_session_control in
    "restart qtile")
        qtile cmd-obj -o cmd -f restart;;
    "shutdown qtile")
        qtile cmd-obj -o cmd -f shutdown;;
    poweroff)
        loginctl poweroff;;
    reboot)
        loginctl reboot;;
    suspend)
        sudo susp;;
esac

