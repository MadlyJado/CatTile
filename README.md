# CatTile
CatTile is a Qtile Config, created by me, MadlyJado, to suit my daily needs on the linux desktop.

# Dependencies:

```
qtile
kitty
sddm
python-iwlib
python-dbus-next
python-requests
python-psutil
git
base-devel
picom
nitrogen
rofi
polkit-gnome (Optional)
paru (Install by doing git clone https://aur.archlinux.org/paru.git and then using makepkg -si)
```
paru is used for aur dependencies, you can also use yay, which if found at [This link](https://aur.archlinux.org/yay.git). It is an aur repo link, so don't click it, as it is readonly, only copy it, and paste it into a
git clone command.
You can also do each one manually by doing git clone all of the below aur repos, but that is tedious, and better used with an aur helper, but it is all up to you.

# AUR Dependencies
```
ttf-nerd-font 
ttf-weather-icons 
qtile-extras
```

# Usage:

To use CatTile, make sure to copy all of the files to .config/qtile, and then, copy picom.conf to /etc/xdg/picom.conf, to overwrite the existing config, to allow for a transparent qtile bar.

In the qtile config, make sure to set your web browser to your web browser of choice.
Make a file called owm_apikey.py, in the qtile config folder in .config/qtile, then make a variable called apikey, and set it to a string containing your api key from [OpenWeatherMap](https://openweathermap.org)
After doing that and installing all of the dependencies, it should work.
You can also optionally add catppuccin themes to kitty config, and spotify using spicetify, using the added optional script. It will install both spicetify and kitty theme, so if you wish to just install kitty config, just
go to the [Catppuccin Kitty Github Repo](https://github.com/catppuccin/kitty)
