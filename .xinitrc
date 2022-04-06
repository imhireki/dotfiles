#!/bin/sh

# Resourcess
xrdb -merge "$HOME/.Xresources"

# Keymap
setxkbmap -option caps:none
xmodmap "$HOME/.Xmodmap"

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

xrandr --output VGA-0 --mode 1360x768 --panning 1700x960 --scale 1.25 &
exec qtile start
