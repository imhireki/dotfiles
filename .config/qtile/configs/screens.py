from libqtile.config import Screen

from . import bars


wallpaper = '~/pictures/wallpapers/8198406.jpg'
# wallpaper = '~/pictures/wallpapers/898789.jpg'

main_screen = Screen(
    top=bars.top_bar,
    wallpaper=wallpaper,
    wallpaper_mode='fill')

SCREENS = [main_screen]

