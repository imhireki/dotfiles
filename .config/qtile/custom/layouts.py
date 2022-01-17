from libqtile.layout.base import _SimpleLayoutBase
from libqtile.layout.xmonad import MonadTall


class Max(_SimpleLayoutBase):
    def __init__(self, **config):
        self.border_width = config.get('border_width')
        self.border_focus = config.get('border_focus')
        self.margin = config.get('margin')

        _SimpleLayoutBase.__init__(self, **config)

    def add(self, client):
        """
        WHEN: whenever a WINDOW is added to a GROUP and the LAYOUT is FOCUSED or
              not
        DO:   add the WINDOW to LAYOUT
        """

        # If a new window = new client(offsetted to focus)
        return super().add(client,
                           offset_to_current=1)

    def configure(self, client, screen_rect):
        # place() -  WINDOW CMD command
        # | X |  Y | width | heght | borderwidth | above | margin |
        # | 0 | 28 |  1920 |  1080 |           2 | False |      8 |
        client.place(screen_rect.x,
                     screen_rect.y,
                     screen_rect.width - 2 * self.border_width,
                     screen_rect.height - 2 * self.border_width,
                     self.border_width,
                     self.border_focus,
                     False,
                     self.margin
                     )

        # "Focus" management
        if self.clients and client is self.clients.current_client:
            client.unhide()
        else:
            client.hide()

    # redirect [M4] command to its functions
    cmd_previous = _SimpleLayoutBase.previous
    cmd_next = _SimpleLayoutBase.next

    cmd_up = cmd_previous
    cmd_down = cmd_next

class MaxFocus(Max): ...

class MonadFocus(MonadTall): ...
