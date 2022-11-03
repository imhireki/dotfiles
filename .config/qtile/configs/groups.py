from libqtile.config import Group, Match


browser = Match(wm_class='qutebrowser')
emacs = Match(wm_class='Emacs')
discord = Match(wm_class='discord')
alacritty = Match(wm_class='Alacritty')
mpv = Match(wm_class='mpv')

GROUPS = [
    Group('a', label='\uf488', layout='max', matches=[browser, mpv]),
    Group('s', label='\uf0f6', layout='monadfocus'),
    Group('d', label='\uf489', layout='monad', matches=[alacritty]),
    Group('f', label='\uf869', layout='monad', matches=[discord]),
    Group('z', label='\uf884', layout='monad'),
    Group('x', label='\uf878', layout='floating'),
    Group('c', label='\uf755', layout='monad'),
    Group('v', label='\uf24a', layout='monad', matches=[emacs]),
]

