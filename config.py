# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import bar, layout, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import libqtile.widget as wg
import owm
from libqtile import qtile
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

# This stands for the windows key/Super key, if you wish to use something else
# Look up which keys stand for what on the qtile docs!
mod = "mod4"
# If you use a different terminal, feel free to change this!
terminal = "kitty"
# Change if you wish to use something other than vivaldi!
myBrowser = "floorp"
# Change this if you have a different name for your wifi interface
myWifi = "wlp5s0"

# Change this if you are using a laptop instead of a desktop
isLaptop = False

def RofiOrWofiDMenu():
    if qtile.core.name== "x11":
        return "rofi -show run"
    elif qtile.core.name == "wayland":
        return "wofi --allow-images --show run"
dmenuCmd = RofiOrWofiDMenu()
def RofiOrWofiDRun():
    if qtile.core.name == "x11":
        return "rofi -show drun"
    elif qtile.core.name == "wayland":
        return "wofi --allow-images --show drun"
drunCmd = RofiOrWofiDRun()


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod, "shift"], "m", lazy.window.toggle_maximize(), desc="Toggle maximize"),
    Key([mod, "shift"] , "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod, "shift"], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod, "shift"], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod, "shift"], "Up", lazy.layout.down(), desc="Move focus down"),
    Key([mod, "shift"], "Down", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], 'w', lazy.spawn('firefox'), desc="Launch firefox"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "control", "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "control", "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "control", "shift"], "Up", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control", "shift"], "Down", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Up", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Down", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawn(dmenuCmd), desc="Open rofi"),
    Key([mod, "control"], "d", lazy.spawn(drunCmd), desc="Open rofi in desktop file opener mode"),
    Key([mod, "shift"], "w", lazy.spawn("rofi -show window"), desc="Open rofi in window opener mode"),
    Key([mod], "b", lazy.spawn(myBrowser), desc="Opens default browser!"),
]

groups = [Group(i) for i in ["", "󰖟", "", "", "󰙯", "󰓓", "", ""]]
group_hotkeys = "123456789"


for g, k in zip(groups, group_hotkeys):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod, "shift"],
                k,
                lazy.group[g.name].toscreen(),
                desc=f"Switch to group {g.name}",
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift", "control"],
                k,
                lazy.window.togroup(g.name, switch_group=False),
                desc="Switch to & move focused window to group {g.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
        ]
    )

layouts = [
    layout.MonadTall(
        margin=20,
        border_width=2
        ),
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Colors
catpuccin = {
        'Rosewater': '#f4dbd6',
        'Flamingo': '#f0c6c6',
        'Pink': '#f5bde6',
        'Mauve': '#c6a0f6',
        'Red': '#ed8796',
        'Maroon': '#ee99a0',
        'Peach': '#f5a97f',
        'Yellow': '#eed49f',
        'Green': '#a6da95',
        'Teal': '#8bd5ca',
        'Sky': '#91d7e3',
        'Sapphire': '#7dc4e4',
        'Blue': '#8aadf4',
        'Lavender': '#b7bdf8',
        'Text': '#cad3f5',
        'Subtext1': '#b8c0e0',
        'Subtext0': '#a5adcb',
        'Overlay2': '#939ab7',
        'Overlay1': '#8087a2',
        'Overlay0': '#6e738d',
        'Surface2': '#5b6078',
        'Surface1': '#494d64',
        'Surface0': '#363a4f',
        'Base': '#24273a',
        'Mantle': '#1e2030',
        'Crust': '#181926'

        

        }

widget_defaults = dict(
        font="hack",
        fontsize=16,
)
extension_defaults = widget_defaults.copy()

# Filters Long file paths for Neovim and Vivaldi long names for website title's
def filterLongWindowNames(text):
    for string in ["NVIM", "Ablaze Floorp"]:
        if string in text:
            if string == "NVIM":
                text = "Neovim"
            elif string == "Ablaze Floorp":
                text = "Floorp Browser"
            else:
                text = string
        else:
            text = text
    return text

networkIcons = ["󰣼", "󰣺"]

# Create function to make triangleWidget easier
def triangleWidget(endOfWidget=False, widget=widget, color=""):
    if(endOfWidget == False):
        return widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=color
            )
                
    return widget.TextBox(
        text = "",
        padding=0,
        fontsize=30,
        foreground=color,
        )

powerline = {
    "decorations": [
         PowerLineDecoration(path='forward_slash'),
    ]
}

def get_widgets(primary=False, isLaptop=False):
    widgets = [
        widget.GroupBox(
            highlight_method="line",
            background=catpuccin["Flamingo"],
            foreground="#00000000",
            highlight_color=[catpuccin["Flamingo"], catpuccin["Flamingo"]],
            inactive=catpuccin["Crust"],
            **powerline
            ),
        widget.WindowName(
            padding=0,
            foreground=catpuccin["Crust"],
            background=catpuccin["Teal"],
            fontsize=10,
            width=470,
            parse_text=filterLongWindowNames,
            **powerline
            ),
        widget.Clock(
            format="     %Y-%m-%d %a %I:%M %p",
            fontsize=10,
            background=catpuccin["Mauve"],
            foreground=catpuccin["Crust"],
            **powerline
            ),
        widget.WiFiIcon(
            background=catpuccin["Green"],
            foreground=catpuccin["Crust"],
            active_colour=catpuccin["Crust"],
            interface=myWifi,
            show_ssid=True,
            font="hack",
            fontsize=10,
            **powerline
            ),
        widget.CheckUpdates(
            background=catpuccin["Green"],
            color_have_updates=catpuccin["Crust"],
            color_no_updates=catpuccin["Crust"],
            foreground=catpuccin["Crust"],
            fontsize=15,
            display_format="󰣇: {updates}",
            distro="Arch_paru",
            **powerline
            ),
        widget.CPU(
            background=catpuccin["Red"],
            fontsize=10,
            format="CPU: {freq_current}GHz {load_percent}%",
            foreground=catpuccin["Crust"],
            ),
        widget.ThermalSensor(
            tag_sensor='Tctl',
            threshold=40.0,
            fontsize=10,
            background=catpuccin["Red"],
            foreground=catpuccin["Crust"],
            ),
        widget.Memory(
            format='Memory: {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm} Swap: {SwapUsed: .0f}{ms}/{SwapTotal: .0f}{ms}',
            fontsize=10,
            background=catpuccin["Red"],
            foreground=catpuccin["Crust"],
            **powerline
            ),
        owm.OpenWeatherMap(
            background=catpuccin["Lavender"],
            foreground=catpuccin["Crust"],
            fontsize=10,
            **powerline,
            ),
        widget.TextBox(
            background=catpuccin["Lavender"],
            text=".",
            fontsize=-6,
            foreground=catpuccin["Lavender"],
            **powerline
        ),
    ]


    if isLaptop and primary:
        widgets = [
                widget.GroupBox(
                    highlight_method="line",
                    background=catpuccin["Flamingo"],
                    foreground="#00000000",
                    highlight_color=[catpuccin["Flamingo"], catpuccin["Flamingo"]],
                    inactive=catpuccin["Crust"],
                    **powerline
                    ),
                widget.WindowName(
                    padding=0,
                    foreground=catpuccin["Crust"],
                    background=catpuccin["Teal"],
                    fontsize=10,
                    width=470,
                    parse_text=filterLongWindowNames,
                    **powerline
                    ),
                widget.Clock(
                    format="     %Y-%m-%d %a %I:%M %p",
                    fontsize=10,
                    background=catpuccin["Mauve"],
                    foreground=catpuccin["Crust"],
                    **powerline
                   ),
                widget.WiFiIcon(
                    background=catpuccin["Green"],
                    foreground=catpuccin["Crust"],
                    active_colour=catpuccin["Crust"],
                    interface=myWifi,
                    show_ssid=True,
                    font="hack",
                    fontsize=10,
                    **powerline
                   ),
                widget.CheckUpdates(
                    background=catpuccin["Green"],
                    color_have_updates=catpuccin["Crust"],
                    color_no_updates=catpuccin["Crust"],
                    foreground=catpuccin["Crust"],
                    fontsize=15,
                    display_format="󰣇: {updates}",
                    distro="Arch_paru",
                    **powerline
                  ),
                widget.CPU(
                        background=catpuccin["Red"],
                        fontsize=10,
                        format="CPU: {freq_current}GHz {load_percent}%",
                        foreground=catpuccin["Crust"],
                  ),
                widget.ThermalSensor(
                    tag_sensor='Tctl',
                    threshold=40.0,
                    fontsize=10,
                    background=catpuccin["Red"],
                    foreground=catpuccin["Crust"],
                    ),
                widget.Memory(
                    format='Memory: {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm} Swap: {SwapUsed: .0f}{ms}/{SwapTotal: .0f}{ms}',
                    fontsize=10,
                    background=catpuccin["Red"],
                    foreground=catpuccin["Crust"],
                    **powerline
                    ),
                owm.OpenWeatherMap(
                    background=catpuccin["Lavender"],
                    foreground=catpuccin["Crust"],
                    fontsize=10,
                    **powerline,
                    ),
                widget.TextBox(
                    background=catpuccin["Lavender"],
                    text=".",
                    fontsize=-6,
                    foreground=catpuccin["Lavender"],
                    **powerline
                    ),
                widgets.append(wg.Systray())
            
        ]
    elif isLaptop and primary == False:
        widgets = [
                widget.GroupBox(
                    highlight_method="line",
                    background=catpuccin["Flamingo"],
                    foreground="#00000000",
                    highlight_color=[catpuccin["Flamingo"], catpuccin["Flamingo"]],
                    inactive=catpuccin["Crust"],
                    **powerline
                    ),
                widget.WindowName(
                    padding=0,
                    foreground=catpuccin["Crust"],
                    background=catpuccin["Teal"],
                    fontsize=10,
                    width=470,
                    parse_text=filterLongWindowNames,
                    **powerline
                    ),
                widget.Clock(
                    format="     %Y-%m-%d %a %I:%M %p",
                    fontsize=10,
                    background=catpuccin["Mauve"],
                    foreground=catpuccin["Crust"],
                    **powerline
                   ),
                widget.WiFiIcon(
                    background=catpuccin["Green"],
                    foreground=catpuccin["Crust"],
                    active_colour=catpuccin["Crust"],
                    interface=myWifi,
                    show_ssid=True,
                    font="hack",
                    fontsize=10,
                    **powerline
                   ),
                widget.CheckUpdates(
                    background=catpuccin["Green"],
                    color_have_updates=catpuccin["Crust"],
                    color_no_updates=catpuccin["Crust"],
                    foreground=catpuccin["Crust"],
                    fontsize=15,
                    display_format="󰣇: {updates}",
                    distro="Arch_paru",
                    **powerline
                  ),
                widget.CPU(
                        background=catpuccin["Red"],
                        fontsize=10,
                        format="CPU: {freq_current}GHz {load_percent}%",
                        foreground=catpuccin["Crust"],
                  ),
                widget.ThermalSensor(
                    tag_sensor='Tctl',
                    threshold=40.0,
                    fontsize=10,
                    background=catpuccin["Red"],
                    foreground=catpuccin["Crust"],
                    ),
                widget.Memory(
                    format='Memory: {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm} Swap: {SwapUsed: .0f}{ms}/{SwapTotal: .0f}{ms}',
                    fontsize=10,
                    background=catpuccin["Red"],
                    foreground=catpuccin["Crust"],
                    **powerline
                    ),
                owm.OpenWeatherMap(
                    background=catpuccin["Lavender"],
                    foreground=catpuccin["Crust"],
                    fontsize=10,
                    **powerline,
                    ),
            widget.TextBox(
                background=catpuccin["Lavender"],
                text=".",
                fontsize=-6,
                foreground=catpuccin["Lavender"],
                **powerline
                ),
                widgets.append(wg.Systray())
        ]
    elif primary and isLaptop == False:
        widgets.append(wg.Systray())
        return widgets
    
    return widgets



screens = [
    Screen(
        top=bar.Bar(
            get_widgets(primary=True, isLaptop=isLaptop),
            22,
            background="#00000000",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            opacity=1,
            ),    
        ),
    Screen(
        top=bar.Bar(
            get_widgets(primary=False, isLaptop=isLaptop),
            22,
            background="#00000000",
            opacity=1,
        )
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "CatTile"

@hook.subscribe.startup_once
def autostart():
    if qtile.core.name == "x11":
        home = os.path.expanduser('~/.config/qtile/autostart.sh')
        subprocess.Popen([home])
    elif qtile.core.name == "wayland":
        home = os.path.expanduser('~/.config/qtile/autostart_wayland.sh')
        subprocess.Popen([home])

def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)



keys.extend([
    Key([mod,"shift"],  "comma",  lazy.function(window_to_next_screen)),    
    Key([mod,"shift"],  "period", lazy.function(window_to_previous_screen)),
    Key([mod,"control"],"comma",  lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod,"control"],"period", lazy.function(window_to_previous_screen, switch_screen=True)),
]
)
