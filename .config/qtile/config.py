from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile import bar, layout, widget, qtile, hook
from libqtile.log_utils import logger
from libqtile.lazy import lazy
from custom.layouts import Focus

M4 = 'mod4'
M1 = 'mod1'

keys = [
    # Move window focus
    Key([M4], "h", lazy.layout.left()),
    Key([M4], "l", lazy.layout.right()),
    Key([M4], "j", lazy.layout.down()),
    Key([M4], "k", lazy.layout.up()),
    Key([M4], "space", lazy.layout.next()),

    # Move the window
    Key([M4, "shift"], "h", lazy.layout.shuffle_left()),
    Key([M4, "shift"], "l", lazy.layout.shuffle_right()),
    Key([M4, "shift"], "j", lazy.layout.shuffle_down()),
    Key([M4, "shift"], "k", lazy.layout.shuffle_up()),

    # Resize the Windows
    Key([M4], 'u', lazy.layout.shrink()),
    Key([M4], 'i', lazy.layout.grow()),
    Key([M4], "o", lazy.layout.maximize()),
    Key([M4], "y", lazy.layout.normalize()),
    
    # Print ( date +  clipboard yank )
    Key([M4], 'p', lazy.spawn('./scripts/print.sh')),
    Key([M4, 'shift' ], 'p', lazy.spawn('./scripts/print_select.sh')),

    # Functions
    Key([M4], "q", lazy.window.kill()),
    Key([M4], "w", lazy.next_layout()),
    Key([M4], "e", lazy.hide_show_bar()),
    Key([M4], 'r', lazy.spawncmd()),

    # Apps
    Key([M1], '1', lazy.spawn("kitty")),
    Key([M1], '2', lazy.spawn("emacsclient -c -a 'emacs'")),
    Key([M1], '3', lazy.spawn('librewolf')),

    # Volume
    Key([M1], 'q', lazy.spawn('amixer -q -D pulse set Master 10%-')),
    Key([M1], 'w', lazy.spawn('amixer -q -D pulse set Master 10%+')),
    Key([M1], 'e', lazy.spawn('amixer -q -D pulse set Master toggle')),

    # Scripts
    Key([M1], 'h', lazy.spawn('sudo ./scripts/clear_drop_caches.sh')),

    # Qtile Managemant
    Key([M1, 'control'], '1', lazy.restart()),
    Key([M1, 'control'], '2', lazy.shutdown()),

    # Session
    Key([M1, 'control'], '3', lazy.spawn('shutdown now')),
    Key([M1, 'control'], '4', lazy.spawn('reboot')),
]

groups = [
    Group(name=n, label=l)
    for n, l in [('a', '一'),
                 ('s', '二'),
                 ('d', '三'),
                 ('f', '四'),
                 ('g', '五'),
                 ('z', '六'),
                 ('x', '七'),
                 ('c', '八'),
                 ('v', '九'),
                 ('b', '十')]
    ]

for i in groups:
    keys.extend([
        # Switch to a group
        Key([M4], i.name, lazy.group[i.name].toscreen()),

        # Move focused to a group
        Key([M4, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False)),
    ])

palette = ['#fcaecb',
           '#b4e6ff',
           '#43a3e2',
           '#ff3030',
           '#7b68ee',
           '#006400',
           '#ffa500',
           '#171717']

layouts = [
    layout.MonadTall(
        border_width=2,
        margin=8,
        border_focus=palette[0],
        border_normal=palette[1],
        ratio=0.6
    ),
    Focus(
        margin=8,
        border_width=2,
        border_focus=palette[1]
    )
]

widget_defaults = dict(
    font='FiraCode',
    fontsize=14,
    padding=1,
    )

extension_defaults = widget_defaults.copy()

textbox = {'fontsize': '20',
           'padding': 0}

top_bar = bar.Bar(
    size=20,
    opacity=1,
    margin=[8, 8, 0, 8],

    widgets = [
        widget.TextBox(
            text=" ",
            **textbox,
            background=palette[0]
            ),

        widget.Image(
            filename='~/Pictures/nyarch.png',
            background=palette[0]
            ),

        widget.Prompt(
            background=palette[0],
            foreground=palette[7],
            prompt='$ '
            ),

        widget.TextBox(
            text="\uE0B0",
            **textbox,
            foreground=palette[0],
            background=palette[1]
            ),

        widget.GroupBox(
            highlight_method='line',
            font='FiraCode Bold',
            fontsize=16,
            margin=5,

            highlight_color=[palette[1], palette[0]],
            this_current_screen_border=palette[0],

            inactive=palette[7],
            active=palette[0],

            background=palette[1],
            ),

        widget.TextBox(
            text="\uE0B2",
            **textbox,
            background=palette[1],
            foreground=palette[2]
            ),

        widget.WindowName(
            empty_group_string='hireki@archwaifu',
            background=palette[2],
            foreground=palette[7]
            ),

        widget.TextBox(
            text="\uE0B2",
            **textbox,
            background=palette[2],
            foreground=palette[7]
            ),

        widget.CPU(
            format='[CPU ({freq_current}Ghz) {load_percent}%',
            background=palette[7],
            foreground=palette[3]
            ),

        widget.ThermalSensor(
            fmt='{} ]',
            background=palette[7],
            foreground=palette[3
]),

        widget.Memory(
            format="[ RAM {MemUsed: .0f}M ]",
            measure_mem="M",
            background=palette[7],
            foreground=palette[4]
            ),

        widget.NvidiaSensors(
            format="[ GPU {temp}°C ]",
            background=palette[7],
            foreground=palette[5]
            ),

        widget.PulseVolume(
            fmt='[ VOL {} ]',
            background=palette[7],
            foreground=palette[6]
            ),

        widget.TextBox(
            text="\uE0B2",
            **textbox,
            background=palette[7],
            foreground=palette[2]
            ),

        widget.Systray(background=palette[2]),

        widget.Clock(
            format='%a %d %b %I:%M %p',
            background=palette[2],
            foreground=palette[7])
        ])

main_screen = Screen(top_bar)
screens = [main_screen]

mouse = [
    Drag([M4], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([M4], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([M4], "Button2", lazy.window.bring_to_front())
]

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

@hook.subscribe.layout_change
def change_change(layout, group):
    """ Hide bar when in Focus layout """
    if layout.name == 'focus':
        if group.screen.top.size != 0:
            qtile.cmd_hide_show_bar()
    else:
        if group.screen.top.size == 0:
            qtile.cmd_hide_show_bar()
