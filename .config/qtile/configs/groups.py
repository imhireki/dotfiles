from libqtile.config import Group, Match


GROUPS = [
    Group('a', label='\uf488', layout='maxfocus', matches=[
        Match(wm_class='qutebrowser'),
        Match(title='browser_player', wm_class='mpv')
        ]),
    Group('s', label='\uf121', layout='monadfocus', matches=[
        Match(wm_class='neovim')
        ]),
    Group('d', label='\uf489', layout='monadfocus', matches=[
        Match(wm_class='Alacritty')
        ]),
    Group('f', label='\uea78', layout='monadwidefocus', matches=[
        Match(wm_class='stig')
        ]),
    Group('z', label='\uf884', layout='monadwidefocus', matches=[
        Match(wm_class='ncmpcpp')
        ]),
    Group('x', label='\uf878', layout='floatingfocus'),
    Group('c', label='\uf755', layout='monadfocus', matches=[
        Match(wm_class='mpv'),
        Match(wm_class='ranger'),
        Match(wm_class='Gimp')
        ]),
    Group('v', label='\uf4a0', layout='monadfocus', matches=[
        Match(wm_class='notebook')
        ]),
]
