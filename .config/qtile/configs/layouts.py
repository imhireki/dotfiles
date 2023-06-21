# type: ignore

from libqtile.layout import Floating, MonadWide

from custom.layouts import (
    Max, MaxFocus, Monad, MonadFocus, MonadWideFocus, FloatingFocus
    )
from extra.palettes import PALETTE


monad_options = {
    'border_width': 3,
    'margin': 10,
    'border_focus': PALETTE[2],
    'border_normal': PALETTE[3],
    'align': 1,
    'max_ratio': 0.65,
    'min_ratio': 0.35,
    'change_ratio': 0.01,
    'min_secondary_size': 245
}

max_options = {
    'margin': 10,
    'border_width': 3,
    'border_focus': PALETTE[3]
}

floating_options = {
    'border_focus': PALETTE[2],
    'border_normal': PALETTE[3],
    'border_width': 3,
}

LAYOUTS = [
    Monad(**monad_options),
    MonadFocus(**monad_options),
    MonadWide(**monad_options),
    MonadWideFocus(**monad_options),
    Max(**max_options),
    MaxFocus(**max_options),
    Floating(**floating_options),
    FloatingFocus(**floating_options),
]

FLOATING_LAYOUT = LAYOUTS[6]

