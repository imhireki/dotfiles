from configs import (
    keys as keys_config,
    groups as groups_config,
    layouts as layouts_config,
    bars as bars_config,
    screens as screens_config,
)
from configs.hooks import *


keys = keys_config.KEYS

mouse = keys_config.MOUSE

groups = groups_config.GROUPS

layouts = layouts_config.LAYOUTS

floating_layout = layouts_config.FLOATING_LAYOUT

widget_defaults = bars_config.WIDGET_DEFAULTS

extension_defaults = widget_defaults.copy()

screens = screens_config.SCREENS

dgroups_key_binder = None

dgroups_app_rules = []

follow_mouse_focus = True

bring_front_click = False

cursor_warp = False

auto_fullscreen = True

focus_on_window_activation = 'smart'

reconfigure_screens = True

auto_minimize = True

wmname = 'LG3D'

