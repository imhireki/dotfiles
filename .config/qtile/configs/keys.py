from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy

from . import groups


m4 = 'mod4'


KEYS = []

MOUSE = [
    Drag([m4], 'Button1', lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([m4], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([m4], "Button2", lazy.window.disable_floating())
]

window_focus_keys = [
    Key([m4], "h", lazy.layout.left()),
    Key([m4], "j", lazy.layout.down()),
    Key([m4], "k", lazy.layout.up()),
    Key([m4], "l", lazy.layout.right()),
]

window_movement_keys = [
    Key([m4, "shift"], "h", lazy.layout.shuffle_left()),
    Key([m4, "shift"], "j", lazy.layout.shuffle_down()),
    Key([m4, "shift"], "k", lazy.layout.shuffle_up()),
    Key([m4, "shift"], "l", lazy.layout.shuffle_right()),
]

window_management_keys = [
    Key([m4], "b", lazy.hide_show_bar()),
    Key([m4, 'control'], 'f', lazy.window.toggle_fullscreen()),
    Key([m4], "q", lazy.window.kill()),
    Key([m4], 'u', lazy.layout.shrink()),
    Key([m4], 'i', lazy.layout.grow()),
    Key([m4], "o", lazy.layout.maximize()),
    ]

menus_keys = [
    Key([m4], 'y', lazy.spawn('.config/qtile/menus/reset_layout.sh')),
    Key([m4], 'p', lazy.spawn('.config/qtile/menus/change_layout.sh')),

    Key([m4], 'r', lazy.spawn('rofi -show run')),
    Key([m4], 'w', lazy.spawn('.config/qtile/menus/run_apps.sh')),
    Key([m4], 'e', lazy.spawn('.config/qtile/menus/run_scripts.sh')),

    Key([m4, 'control'], 's', lazy.spawn('.config/qtile/menus/control_session.sh')),
]

audio_keys = [
    Key([m4], 'equal', lazy.widget['pulsevolume'].increase_vol(5)),
    Key([m4], 'minus', lazy.widget['pulsevolume'].decrease_vol(5)),
    Key([m4], 'm', lazy.widget['pulsevolume'].mute()),
]

for keys in [
        window_focus_keys,
        window_movement_keys,
        window_management_keys,
        menus_keys,
        audio_keys,
        ]:
    KEYS.extend(keys)

for group in groups.GROUPS:
    KEYS.extend([
        Key([m4], group.name, lazy.group[group.name].toscreen()),
        Key([m4, 'shift'], group.name,
            lazy.window.togroup(group.name, switch_group=False))
    ])

