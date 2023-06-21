from libqtile.config import Group, Match

import os


GROUPS = [
    Group('a', label='\uf488', layout='maxfocus', matches=[
        Match(wm_class='firefox'),
        Match(title='browser_player', wm_class='mpv'),
        ]),
    Group('s', label='\uf121', layout='monadfocus', matches=[
        Match(wm_class='helix')
        ]),
    Group('d', label='\uf489', layout='monadfocus', matches=[
        Match(wm_class='Alacritty')
        ]),
    Group('f', label='\uf1d9', layout='monadwidefocus', matches=[
        Match(wm_class='discord')
        ]),
    Group('z', label='\uf001', layout='monadwidefocus', matches=[
        Match(wm_class='ncmpcpp'),
        Match(wm_class='pulsemixer'),
        ]),
    Group('x', label='\uf108', layout='floatingfocus', matches=[
        Match(func=lambda c: c.has_fixed_size()),
        Match(func=lambda c: c.has_fixed_ratio()),
        Match(wm_type="utility"),
        Match(wm_type="notification"),
        Match(wm_type="toolbar"),
        Match(wm_type="splash"),
        Match(wm_type="dialog"),
        Match(wm_class="file_progress"),
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        ]),
    Group('c', label='\uf0a0', layout='monadfocus', matches=[
        Match(wm_class='mpv'),
        Match(wm_class='lf'),
        Match(wm_class='MuPDF'),
        ]),
    Group('v', label='\uf4a0', layout='monadfocus', matches=[
        Match(wm_class='notebook')
        ]),
]
