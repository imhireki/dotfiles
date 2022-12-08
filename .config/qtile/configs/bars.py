# type: ignore

from libqtile import bar, widget

from extra.palettes import PALETTE
# from custom.widgets import AnimatedText


WIDGET_DEFAULTS = dict(
    font='Caskaydia Cove Nerd Font',
    fontsize=14,
    padding=1,
)

images = '~/.config/qtile/extra/images'

textbox_options = {
    'fontsize': 20,
    'padding': 0
}

widgets = [
    widget.Image(
        filename=f'{images}/kusanagi.png',
        background=PALETTE[2],
        margin_x=5),
    widget.TextBox(
        fontsize=20,
        padding=0,
        text="\ue0c0 ",
        background=PALETTE[0],
        foreground=PALETTE[2]),
    widget.GroupBox(
        font='FiraCode',
        fontsize=28,
        margin=3,
        highlight_method='line',
        highlight_color=PALETTE[0],
        this_current_screen_border=[PALETTE[4]],
        background=PALETTE[0],
        inactive=PALETTE[1],
        active=PALETTE[5]),
    widget.TextBox(
        **textbox_options,
        text="\ue0c0 ",
        background=PALETTE[3],
        foreground=PALETTE[0]),
    widget.Spacer(
        background=PALETTE[3],
    ),
    # AnimatedText(
    #     text_list=[
    #         '🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 '
    #         '🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪',
    #         # '🔸 🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹'
    #         # '🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸',
    #         # '🔹 🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸'
    #         # '🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹',
    #     ],
    #     width=bar.STRETCH,
    #     background=PALETTE[3],
    #     foreground=PALETTE[0]),
    widget.TextBox(
        **textbox_options,
        text="\uE0B3\uE0B2",
        background=PALETTE[3],
        foreground=PALETTE[0]),
    widget.Image(
        margin=2,
        filename=f'{images}/cpu2.png',
        background=PALETTE[0]),
    widget.CPU(
        format=' ({freq_current}Ghz) {load_percent}%',
        background=PALETTE[0],
        foreground=PALETTE[1]),
    widget.Image(
        margin=2,
        filename=f'{images}/thermometer2.png',
        background=PALETTE[0]),
    widget.ThermalSensor(
        fmt='{}  ',
        background=PALETTE[0],
        foreground=PALETTE[1]),
    widget.TextBox(
        text="\uE0B9\uE0B3 ",
        **textbox_options,
        background=PALETTE[0],
        foreground=PALETTE[4]),
    widget.Image(
        filename=f'{images}/ram2.png',
        background=PALETTE[0]),
    widget.Memory(
        format="{MemFree: .0f}M ",
        measure_mem="M",
        background=PALETTE[0],
        foreground=PALETTE[1]),
    widget.TextBox(
        text="\uE0bd\uE0B3 ",
        **textbox_options,
        background=PALETTE[0],
        foreground=PALETTE[5]),
    widget.Image(
        margin=2,
        filename=f'{images}/vga-card2.png',
        background=PALETTE[0]),
    widget.NvidiaSensors(
        format="{temp}°C",
        padding=10,
        background=PALETTE[0],
        foreground=PALETTE[1]),
    widget.TextBox(
        text="\uE0B9\uE0B3 ",
        **textbox_options,
        background=PALETTE[0],
        foreground=PALETTE[4]),
    widget.Image(
        margin=2,
        filename=f'{images}/headphones2.png',
        background=PALETTE[0]),
    widget.PulseVolume(
        fmt='{}',
        padding=10,
        background=PALETTE[0],
        foreground=PALETTE[1]),
    widget.TextBox(
        text="\uE0Bd\uE0B3 ",
        **textbox_options,
        background=PALETTE[0],
        foreground=PALETTE[5]),
    widget.Systray(background=PALETTE[0]),
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

