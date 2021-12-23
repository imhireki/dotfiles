from typing import List

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import qtile

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch Between Windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move focus next"),

    # Move the Windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="M/ left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="M/ right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="M/ down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="M/ up"),

    # Resize the Windows
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),

    # Apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod], "e", lazy.spawn("emacsclient -c -a 'emacs'")),

    # Functions
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "b", lazy.hide_show_bar()),
]

groups = [
    Group(name=n, label=l)
    for n, l in
    [
        (str(n), l)
        for n,l in enumerate(['一', '二', '三', '四', '五'], 1)
    ]
]

for i in groups:
    keys.extend([
        # Switch to a group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # Move focused to a group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False)),
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
        widget.Image(filename='~/penguin.png'),

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

        widget.TextBox(text="\uE0B8",
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
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
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

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
