from typing import List

from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

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
    for n, l in
    [
        (str(n), l)
        for n,l in [('a', '一'),
                    ('s', '二'),
                    ('d', '三'),
                    ('f', '四'),
                    ('g', '五')]
    ]
]

for i in groups:
    keys.extend([
        # Switch to a group
        Key([M4], i.name, lazy.group[i.name].toscreen()),

        # Move focused to a group
        Key([M4, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False)),
    ])

layouts = [
    layout.MonadTall(margin=8,
                     border_width=2,
                     border_normal='#D39CDE',
                     border_focus='#608BDF',
                     ratio=0.6),
    layout.Max(),
    layout.Floating(),
]


widget_defaults = dict(
    font='FiraCode Medium',
    fontsize=14,
    padding=3,
    foreground='#000000'
)

extension_defaults = widget_defaults.copy()

colors = {'primary': '#D39CDE',
          'secondary': '#608BDF',
          'font': '#000000'}

standard = {'background' : colors['primary'],
            'foreground' : colors['secondary']}

reverse = {'background' : colors['secondary'],
           'foreground' : colors['primary']}

textbox = {'fontsize': '20',
           'padding': 0}


top_bar = bar.Bar(
    size=20,
    opacity=0.75,
    margin=[8, 8, 0, 8],
    background=colors['primary'],
    widgets = [
        widget.Image(filename='~/Pictures/icon.png'),

        widget.Prompt(foreground=colors['font'],
                      background=colors['primary'],
                      prompt='spell: ',
                      ),

        widget.TextBox(text="\uE0B0",
                       **textbox,
                       **reverse
                       ),

        widget.GroupBox(font='FiraCode Bold',
                        fontsize=16,
                        highlight_method='text',

                        inactive=colors['font'],
                        this_current_screen_border='#FFFFFF',

                        background=colors['secondary'],
                        active=colors['primary'],
                        ),

        widget.TextBox(text="\uE0B0",
                       **textbox,
                       **standard
                       ),

        widget.WindowName(),

        widget.TextBox(text="\uE0BA",
                       **textbox,
                       **standard
                       ),

        widget.CPU(format='CPU ({freq_current}Ghz) {load_percent}%',
                   background=colors['secondary']),

        widget.TextBox(text="\uE0BC",
                       **textbox,
                       **standard
                       ),

        widget.Memory(format="Free {MemFree: .0f}M",
                      measure_mem="M"),

        widget.TextBox(text="\uE0BC",
                       **textbox,
                       **reverse
                       ),

        widget.NvidiaSensors(format="GPU {temp}°C",
                             background=colors['secondary'],
                             foreground=colors['font']),

        widget.TextBox(text="\uE0BC",
                       **textbox,
                       **standard
                       ),

        widget.Systray(background=colors['primary']),

        widget.CurrentLayout(),

        widget.TextBox(text="\uE0BC",
                       **textbox,
                       **reverse
                       ),

        widget.Clock(format='%I:%M %p [ %A ] %m/%d/%Y',
                     background=colors['secondary']),
        ])


main_screen = Screen(top_bar)
screens = [main_screen]

# Drag floating layouts.
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
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
