echo "Adding deb repo to apt sources.d folder"
echo "deb http://ppa.launchpad.net/tycho-s/ppa/ubuntu precise main\ndeb-src http://ppa.launchpad.net/tycho-s/ppa/ubuntu precise main"
echo "Downloading key from ubuntu's server for addition to install qtile"
curl "http://keyserver.ubuntu.com:11371/pks/lookup?op=get&search=0x8516D5EEF453E809" > tyco.key
echo "Adding key to apt"
apt-key add tyco.key
echo "Installing qtile via apt"
apt-get update && apt-get install qtile
echo "Installing qtile bar dependencies, as well as catpuccin theme dependencies"
pip install iwlib psutil --break-system-packages
echo "Installing spicetify"
curl -fsSL https://raw.githubusercontent.com/spicetify/spicetify-cli/master/install.sh | sh
echo "Installing kitty terminal"
apt-get update && apt-get install kitty
echo "Now installing picom"
apt-get update && apt-get install picom
echo "Now installing nitrogen"
apt-get update && apt-get install nitrogen
echo "Now copying qtile config and picom config to their respective folders"
mkdir ~/.config/qtile & 
cp ./config.py ~/.config/qtile/ & 
cp owm.py .config/qtile &
cp autostart.sh ~/.config/qtile &
echo "apikey=''" >> ~/.config/qtile/owm_apikey.py

