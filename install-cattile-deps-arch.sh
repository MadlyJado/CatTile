pacman -Syu qtile python-iwlib python-psutil python-dbus python-dbus-next git base-devel picom nitrogen polkit-gnome rofi --needed
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
paru -S ttf-hack-nerd-font ttf-weather-icons qtile-extras
echo "CatTile Bar dependencies are now fully installed!"
