# type: ignore

from libqtile.layout.base import _SimpleLayoutBase
from libqtile.layout.xmonad import MonadTall
from libqtile.layout.xmonad import MonadWide
from libqtile.layout.floating import Floating
from libqtile.command.base import expose_command


class Max(_SimpleLayoutBase):
    """Maximized layout with borders."""

    def __init__(self, **config) -> None:
        self.border_width = config.get('border_width')
        self.border_focus = config.get('border_focus')
        self.margin = config.get('margin')
        super().__init__(**config)

    def add(self, client) -> None:
        return super().add(client, offset_to_current=1)

    def configure_window_placement(self, client, screen_rect) -> None:
        client.place(screen_rect.x,
                     screen_rect.y,
                     screen_rect.width - 2 * self.border_width,
                     screen_rect.height - 2 * self.border_width,
                     self.border_width,
                     self.border_focus,
                     False,
                     self.margin
                     )

    def configure_window_focus(self, client) -> None:
        if self.clients and client is self.clients.current_client:
            client.unhide()
        else:
            client.hide()

    def configure(self, client, screen_rect) -> None:
        self.configure_window_placement(client, screen_rect)
        self.configure_window_focus(client)

    @expose_command("previous")
    def up(self):
        _SimpleLayoutBase.previous(self)

    @expose_command("next")
    def down(self):
        _SimpleLayoutBase.next(self)


class Monad(MonadTall):
    """MonadTall with improved commands."""

    @expose_command("normalize")
    def normalize(self, redraw=True) -> None:
        """Evenly distribute screen-space among secondary clients"""

        n = len(self.clients) - 1
        if n > 0 and self.screen_rect is not None:
            self.relative_sizes = [1.0 / n] * n
        if redraw:
            self.group.layout_all()
        self.do_normalize = False

    @expose_command("reset")
    def reset(self, redraw=True) -> None:
        """Normalize main and secondary clients"""

        self.ratio = 0.5
        self.normalize(redraw)

    @expose_command("normalize_main")
    def normalize_main(self, redraw=True) -> None:
        """Normalize main client"""
        
        self.ratio = 0.5
        self.group.layout_all()


class MonadFocus(Monad): pass

class MonadWideFocus(MonadWide): pass

class FloatingFocus(Floating): pass

class MaxFocus(Max): pass 


