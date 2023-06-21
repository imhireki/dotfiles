from os.path import expanduser
import subprocess

from libqtile import hook


@hook.subscribe.layout_change
def hide_bar_focus_layout(layout, group):
    """ Hide bar when in some focus layout """
    if group.screen:  # Avoid problems with screen start time.
        bar = group.screen.top.is_show()
        if 'focus' in layout.name:
            if bar is True:
                group.screen.top.show(False)
        else:
            if bar is False:
                group.screen.top.show(True)

