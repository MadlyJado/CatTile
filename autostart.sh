#!/bin/sh
exec picom -f & 
nitrogen --restore &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
sudo mount /dev/sdc1 /crucialexternalssd/
