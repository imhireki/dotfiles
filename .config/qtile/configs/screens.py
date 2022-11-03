from libqtile.config import Screen

from . import bars


wallpaper = '~/.config/qtile/extra/images/1285751.png'

main_screen = Screen(
    top=bars.top_bar,
    wallpaper=wallpaper,
    wallpaper_mode='fill')

SCREENS = [main_screen]

