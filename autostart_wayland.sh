#!/bin/sh
export XDG_CURRENT_DESKTOP="qtile" &
exec "/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1" &
swww-daemon &
swww img -o DP-1 ~/Wallpapers/stretched-1920-1080-1345308.jpeg &
swww img -o DP-2 ~/Wallpapers/485965.jpeg &

