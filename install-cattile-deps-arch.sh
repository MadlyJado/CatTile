echo "Installing non-aur dependencies first!"
pacman -Syu qtile python-iwlib python-psutil python-dbus python-dbus-next git base-devel picom nitrogen polkit-gnome rofi --needed
echo "Installing the paru aur helper to install aur dependencies"
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
echo "Installing aur dependencies"
paru -S ttf-hack-nerd-font ttf-weather-icons qtile-extras
echo "CatTile Bar dependencies are now fully installed!"