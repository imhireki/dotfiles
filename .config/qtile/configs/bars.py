from libqtile import bar, widget

from extra.palettes import PALETTE  # type: ignore


WIDGET_DEFAULTS = dict(
    font='Caskaydia Cove Nerd Font Propo',
    fontsize=13,
    padding=1,
)

widgets = [
    widget.Image(
        filename=f'~/.config/qtile/extra/images/kusanagi.png',
        background=PALETTE[2],
        margin_x=5),
    widget.TextBox(
        fontsize=20,
        padding=0,
        text="\ue0c0",
        background=PALETTE[0],
        foreground=PALETTE[2]),
    widget.GroupBox(
        fontsize=16,
        margin=3,
        highlight_method='line',
        highlight_color=PALETTE[0],
        this_current_screen_border=[PALETTE[4]],
        background=PALETTE[0],
        inactive=PALETTE[1],
        active=PALETTE[2]),
    widget.TextBox(
        fontsize=20,
        padding= 0,
        text="\ue0c0 ",
        background=PALETTE[3],
        foreground=PALETTE[0]),
    widget.Spacer(background=PALETTE[3]),
    widget.TextBox(
        fontsize=20,
        padding=0,
        text="\uE0B3\uE0B2",
        background=PALETTE[3],
        foreground=PALETTE[0]),
    widget.TextBox(
        fontsize=16,
        text="\uf4bc",
        background=PALETTE[0],
        foreground=PALETTE[2]),
    widget.CPU(
        format=' ({freq_current}Ghz) {load_percent}%',
        background=PALETTE[0],
        foreground=PALETTE[1]),
    widget.TextBox(
        fontsize=16,
        text="\uf2c9",
        padding=8,
        background=PALETTE[0],
        foreground=PALETTE[2]),
    widget.ThermalSensor(
        fmt='{} ',
        background=PALETTE[0],
        foreground=PALETTE[1]),
    widget.TextBox(
        fontsize=16,
        text="\ue266",
        background=PALETTE[0],
        foreground=PALETTE[2]),
    widget.Memory(
        format="{MemFree: .0f}M ",
        measure_mem="M",
        background=PALETTE[0],
        foreground=PALETTE[1]),
    widget.TextBox(
        fontsize=16,
        text="\uf11b",
        background=PALETTE[0],
        foreground=PALETTE[2]),
    widget.NvidiaSensors(
        format="{temp}°C",
        padding=10,
        background=PALETTE[0],
        foreground=PALETTE[1]),
    widget.TextBox(
        fontsize=16,
        text="\ue638",
        background=PALETTE[0],
        foreground=PALETTE[2]),
    widget.PulseVolume(
        fmt='{}',
        padding=10,
        background=PALETTE[0],
        foreground=PALETTE[1]),
    widget.Systray(background=PALETTE[0]),
    widget.TextBox(
        fontsize=16,
        text=" \uf073",
        background=PALETTE[0],
        foreground=PALETTE[2]),
    widget.Clock(
        padding=10,
        format='%a %d %b %I:%M %p',
        background=PALETTE[0],
        foreground=PALETTE[1])
]

top_bar = bar.Bar(
    size=22,
    opacity=1,
    widgets=widgets,
    margin=[5,5,0,5]
)

