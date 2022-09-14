from libqtile.config import Click, Drag, Group, Key, Screen, KeyChord
from libqtile import bar, layout, widget, hook
from libqtile.lazy import lazy

from custom.layouts import Max, MaxFocus, MonadFocus, Monad

from os.path import expanduser
import subprocess


M4 = 'mod4'
M1 = 'mod1'

palette = {
    'main': [
        '#de41c4',
        '#282a36',
        '#4c4bff',
        '#a956fe',
    ],
    'base': [
        '#282a36',
        '#f8f8f2'
    ]
}

keys = [
    # Move window focus
    Key([M4], "h", lazy.layout.left()),
    Key([M4], "l", lazy.layout.right()),
    Key([M4], "j", lazy.layout.down()),
    Key([M4], "k", lazy.layout.up()),

    # Move the window
    Key([M4, "shift"], "h", lazy.layout.shuffle_left()),
    Key([M4, "shift"], "l", lazy.layout.shuffle_right()),
    Key([M4, "shift"], "j", lazy.layout.shuffle_down()),
    Key([M4, "shift"], "k", lazy.layout.shuffle_up()),

    # Resize the Windows
    Key([M4], 'u', lazy.layout.shrink()),
    Key([M4], 'i', lazy.layout.grow()),
    Key([M4], "o", lazy.layout.maximize()),
    KeyChord([M4], 'y', [
        Key([], '1', lazy.layout.reset()),
        Key([], '2', lazy.layout.normalize()),
        Key([], '3', lazy.layout.normalize_main())
    ]),

    # Move to layout
    KeyChord([M4], 'w', [
        Key([], '1', lazy.to_layout_index(index=0)),
        Key([], '2', lazy.to_layout_index(index=1)),
        Key([], '3', lazy.to_layout_index(index=2)),
        Key([], '4', lazy.to_layout_index(index=3)),
        Key([], '5', lazy.to_layout_index(index=4)),
    ]),

    Key([M4], 'p', lazy.spawn('./scripts/print.sh')),
    Key([M4], "q", lazy.window.kill()),
    Key([M4], "e", lazy.hide_show_bar()),
    Key([M4], 'r', lazy.spawn("rofi -show run")),

    # Apps
    Key([M1], '1', lazy.spawn("alacritty")),
    Key([M1], '2', lazy.spawn('qutebrowser')),

    # Volume
    Key([M1], 'q', lazy.spawn('amixer -q -D pulse set Master 10%-')),
    Key([M1], 'w', lazy.spawn('amixer -q -D pulse set Master 10%+')),
    Key([M1], 'e', lazy.spawn('amixer -q -D pulse set Master toggle')),

    # Scripts
    Key([M1], 'h', lazy.spawn('sudo ./scripts/clear_drop_caches.sh')),
    KeyChord([M1], 'r', [
        Key([], 'v', lazy.spawn('./scripts/rec.sh video')),
        Key([], 'c', lazy.spawn('./scripts/rec.sh screencast')),
        Key([], 'k', lazy.spawn('./scripts/rec.sh kill')),
    ]),

    # Qtile Managemant
    Key([M1, 'control'], '1', lazy.restart()),
    Key([M1, 'control'], '2', lazy.shutdown()),

    # Session
    Key([M1, 'control'], '3', lazy.spawn('shutdown now')),
    Key([M1, 'control'], '4', lazy.spawn('reboot')),
]

groups = [
    Group(name=n, label=l, layout='monad')
    if n not in ['s', 'x', 'c'] else
    Group(name=n, label=l, layout='monadfocus')
    if n != 'c' else
    Group(name=n, label=l, layout='floating')
    for n, l in [('a', '\ufa9e'),
                 ('s', '\ue7c5'),
                 ('d', '\uf489'),
                 ('f', '\uf233'),
                 ('g', '\uf1c0'),
                 ('z', '\uf1bc'),
                 ('x', '\uf11b'),
                 ('c', '\uf108'),
                 ('v', '\ue5ff'),
                 ('b', '\ue28c')]
]

for i in groups:
    keys.extend([
        Key([M4], i.name, lazy.group[i.name].toscreen()), # switch to group
        Key([M4, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False)), # move to group
])

bar_palette = {
    'icon':   [palette['main'][0], palette['base'][0]],
    'group':  [palette['base'][0], palette['base'][1], palette['main'][0]],
    'spacer': [palette['main'][2]],
    'sys':    [palette['main'][1], palette['base'][1]],
    'clock':  [palette['main'][3], palette['base'][0]]
}

monad_options = {
    'border_width': 3,
    'margin': 10,
    'border_focus': palette['main'][0],
    'border_normal': palette['main'][2],
    'align': 1,
    'max_ratio': 0.65,
    'min_ratio': 0.35,
    'change_ratio': 0.01,
    'min_secondary_size': 245
}

max_options = {
    'margin': 10,
    'border_width': 3,
    'border_focus': palette['main'][2]
}

layouts = [
    Monad(**monad_options),
    MonadFocus(**monad_options),
    Max(**max_options),
    MaxFocus(**max_options),
    layout.Floating(
        border_focus=palette['main'][0],
        border_normal=palette['main'][1],
        border_width=3,
    )
]

floating_layout = layouts[4]

widget_defaults = dict(
    font='FiraCode',
    fontsize=14,
    padding=1,
)

extension_defaults = widget_defaults.copy()

textbox = {'fontsize': 20,
           'padding': 0,
           'font': 'Caskaydia Cove Nerd Font'}

top_bar = bar.Bar(
    size=22,
    opacity=1,
    margin=[5,5,0,5],
    widgets = [
        widget.TextBox(
            text=" ",
            **textbox,
            background=bar_palette['icon'][0]
            ),
        widget.Image(
            filename=f'~/.config/qtile/images/kusanagi.png',
            background=bar_palette['icon'][0]
            ),
        widget.TextBox(
            text="\ue0c0 ",
            **textbox,
            background=bar_palette['group'][0],
            foreground=bar_palette['icon'][0]
            ),
        widget.GroupBox(
            font='FiraCode Bold',
            fontsize=25,
            margin=3,

            highlight_method='line',
            highlight_color=bar_palette['group'][0],
            this_current_screen_border=[bar_palette['group'][2]],

            background=bar_palette['group'][0],
            inactive=bar_palette['group'][1],
            active=bar_palette['group'][2],
            ),
        widget.TextBox(
            text="\ue0c0 ",
            **textbox,
            background=bar_palette['spacer'][0],
            foreground=bar_palette['group'][0]
            ),
        widget.TextBox(
            width=bar.STRETCH,
            text="🔸 🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸",
            foreground=bar_palette['group'][0],
            background=bar_palette['spacer'][0]
            ),
         widget.TextBox(
            text="\uE0B3\uE0B2",
            **textbox,
            background=bar_palette['spacer'][0],
            foreground=bar_palette['sys'][0]
            ),
        widget.TextBox(
            text=" ",
            background=bar_palette['sys'][0],
            foreground=bar_palette['clock'][0]
            ),
        widget.Image(
            margin=2,
            filename=f'~/.config/qtile/images/cpu.png',
            background=bar_palette['sys'][0]
            ),
        widget.CPU(
            format=' ({freq_current}Ghz) {load_percent}%',
            background=bar_palette['sys'][0],
            foreground=bar_palette['sys'][1]
            ),
        widget.Image(
            margin=2,
            filename=f'~/.config/qtile/images/thermometer.png',
            background=bar_palette['sys'][0]
            ),
        widget.ThermalSensor(
            fmt='{}  ',
            background=bar_palette['sys'][0],
            foreground=bar_palette['sys'][1]),
        widget.TextBox(
            text="\uE0B9\uE0B3 ",
            **textbox,
            background=bar_palette['sys'][0],
            foreground=palette['main'][0]
            ),
        widget.Image(
            filename=f'~/.config/qtile/images/ram.png',
            background=bar_palette['sys'][0]
            ),
        widget.Memory(
            format="{MemFree: .0f}M ",
            measure_mem="M",
            background=bar_palette['sys'][0],
            foreground=bar_palette['sys'][1]
            ),
        widget.TextBox(
            text="\uE0bd\uE0B3 ",
            **textbox,
            background=bar_palette['sys'][0],
            foreground=palette['main'][2]
            ),
        widget.Image(
            margin=2,
            filename=f'~/.config/qtile/images/graphics-card.png',
            background=bar_palette['sys'][0]
            ),
        widget.NvidiaSensors(
            format="{temp}°C",
            padding=10,
            background=bar_palette['sys'][0],
            foreground=bar_palette['sys'][1]
            ),
        widget.TextBox(
            text="\uE0B9\uE0B3 ",
            **textbox,
            background=bar_palette['sys'][0],
            foreground=palette['main'][0]
            ),
        widget.Image(
            margin=2,
            filename='~/.config/qtile/images/loud-speaker.png',
            background=bar_palette['sys'][0]
            ),
        widget.PulseVolume(
            fmt='{}',
            padding=10,
            background=bar_palette['sys'][0],
            foreground=bar_palette['sys'][1]
            ),
        widget.TextBox(
            text="\uE0Bd\uE0B3 ",
            **textbox,
            background=bar_palette['sys'][0],
            foreground=palette['main'][2]
            ),
        widget.Systray(background=bar_palette['sys'][0]),
        widget.Clock(
            padding=10,
            format='%a %d %b %I:%M %p',
            background=bar_palette['sys'][0],
            foreground=palette['base'][1]
        ),
        widget.TextBox(
            text="\ue0c0 ",
            **textbox,
            background=palette['main'][2],
            foreground=palette['base'][0]
            ),
    ])

main_screen = Screen(
    top=top_bar,
    wallpaper_mode='fill',
    wallpaper='~/Pictures/wp8312609-aesthetic-jjba-laptop-wallpapers.jpg'
)

screens = [main_screen]

mouse = [
    Drag([M4], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([M4], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([M4], "Button2", lazy.window.bring_to_front())
]

@hook.subscribe.layout_change
def hide_bar_focus_layout(layout, group):
    """ Hide bar when in some focus layout """
    if group.screen: # avoid problems with screen start time
        bar = group.screen.top.is_show()
        if 'focus' in layout.name:
            if bar is True:
                group.screen.top.show(False)
        else:
            if bar is False:
                group.screen.top.show(True)

@hook.subscribe.startup_once
def start_once():
    subprocess.call([expanduser('~/') + '.config/qtile/autostart.sh'])

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = False
auto_minimize = True
wmname = "LG3D"
