# Clone catpuccin kitty repo
git clone https://github.com/catppuccin/kitty.git &
# Copy macchiato kitty theme into kitty config file
cp ./kitty/themes/macchiato.conf ../kitty/kitty.conf &
# Next, clone spicetify catpuccin repo
git clone https://github.com/catppuccin/spicetify.git &
# Copy spicetify theme to spicetify themes folder
cp -r ./spicetify/catppuccin/ ../spicetify/Themes/ &
# Set up spicetify config to use catppuccin spicetify theme
spicetify config current_theme catppuccin &
spicetify config color_scheme macchiato &
spicetify config inject_css 1 inject_theme_js 1 replace_colors 1 overwrite_assets 1 &
spicetify apply;
