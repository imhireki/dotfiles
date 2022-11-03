from libqtile.config import Click, Drag, Key, KeyChord
from libqtile.lazy import lazy

from . import groups


m4 = 'mod4'
m1 = 'mod1'


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
    Key([m4], "e", lazy.hide_show_bar()),
    Key([m4], "q", lazy.window.kill()),

    Key([m4], 'u', lazy.layout.shrink()),
    Key([m4], 'i', lazy.layout.grow()),
    Key([m4], "o", lazy.layout.maximize()),
    KeyChord([m4], 'y', [
        Key([], '1', lazy.layout.reset()),
        Key([], '2', lazy.layout.normalize()),
        Key([], '3', lazy.layout.normalize_main())
    ]),
]

layout_swap_keys = [
    KeyChord([m4], 'w', [
        Key([], '1', lazy.to_layout_index(index=0)),
        Key([], '2', lazy.to_layout_index(index=1)),
        Key([], '3', lazy.to_layout_index(index=2)),
        Key([], '4', lazy.to_layout_index(index=3)),
        Key([], '5', lazy.to_layout_index(index=4)),
    ]),
]

apps_keys = [
    Key([m4], 'r', lazy.spawn('rofi -show run')),
    Key([m1], '1', lazy.spawn('alacritty')),
    Key([m1], '2', lazy.spawn('qutebrowser')),
    Key([m1], '3', lazy.spawn('emacsclient -c -a "emacs"')),
]

audio_keys = [
    Key([m1], 'q', lazy.widget['pulsevolume'].increase_vol(5)),
    Key([m1], 'w', lazy.widget['pulsevolume'].decrease_vol(5)),
    Key([m1], 'e', lazy.widget['pulsevolume'].mute()),
]

scripts_keys = [
    KeyChord([m1], 'r', [
        Key([], 'v', lazy.spawn('./scripts/rec.sh video')),
        Key([], 'c', lazy.spawn('./scripts/rec.sh screencast')),
        Key([], 'k', lazy.spawn('./scripts/rec.sh kill')),
    ]),
    Key([m1], 'h', lazy.spawn('sudo ./scripts/clear_drop_caches.sh')),
    Key([m4], 'p', lazy.spawn('./scripts/print.sh')),
]

qtile_management_keys = [
    Key([m1, 'control'], '1', lazy.restart()),
    Key([m1, 'control'], '2', lazy.shutdown()),
]

session_keys = [
    Key([m1, 'control'], '3', lazy.spawn('shutdown now')),
    Key([m1, 'control'], '4', lazy.spawn('reboot')),
]


for keys in [
        window_focus_keys,
        window_movement_keys,
        window_management_keys,
        layout_swap_keys,
        apps_keys,
        audio_keys,
        scripts_keys,
        qtile_management_keys,
        session_keys
        ]:
    KEYS.extend(keys)

for group in groups.GROUPS:
    KEYS.extend([
        Key([m4], group.name, lazy.group[group.name].toscreen()),
        Key([m4, 'shift'], group.name, 
            lazy.window.togroup(group.name, switch_group=False))
    ])

