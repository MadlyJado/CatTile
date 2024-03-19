#!/bin/sh
exec picom -f & 
nitrogen --restore &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1