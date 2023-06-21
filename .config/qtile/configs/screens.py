from libqtile.config import Screen

from . import bars


main_screen = Screen(
    top=bars.top_bar,
    wallpaper='~/.config/qtile/extra/images/wallpaper.jpg',
    wallpaper_mode='fill')

SCREENS = [main_screen]

