# Change perms in opt/spotify and /opt/spotify/Apps folders to allow spicetify to
# change and edit files in spotify folder for themes
groupadd spicetify
usermod -a -G spicetify $(whomai)
chown spicetify /opt/spotify
chown spicetify /opt/spotify/Apps -R
echo "Fixed Perms in Spotify! Make sure to edit the config file of spicetify in .config/spicetify/config-xpui.ini"
echo "\nTo fix the prefs, which is typically located in .config/spotify/prefs."