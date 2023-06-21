
from libqtile.widget.base import _TextBox
from libqtile.log_utils import logger


class TextBox(_TextBox):
    def update(self, text: str) -> None:
        if text is None:
            text = ""

        old_width = self.layout.width
        self.text = text

        if self.layout.width == old_width:
            self.draw()
        else:
            self.bar.draw()


class ThreadPoolText(TextBox):
    defaults = [(
        "update_interval",
        600,
        "Update interval in seconds, if none, the widget updates whenever it's done.",
    )]

    def __init__(self, text: str, **config) -> None:
        super().__init__(text, **config)
        self.add_defaults(ThreadPoolText.defaults)

    def timer_setup(self) -> None:
        def on_done(future):
            try:
                result = future.result()
            except Exception:
                result = None
                logger.exception("poll() raised exceptions, not rescheduling")

            if result is not None:
                try:
                    self.update(result)

                    if self.update_interval is not None:
                        self.timeout_add(self.update_interval, self.timer_setup)
                    else:
                        self.timer_setup()

                except Exception:
                    logger.exception("Failed to reschedule.")
            else:
                logger.warning("poll() returned None, not rescheduling")

        self.future = self.qtile.run_in_executor(self.poll)
        self.future.add_done_callback(on_done)

    def poll(self) -> None:
        pass


class AnimatedText(ThreadPoolText):
    defaults = [("update_interval", 0.5, "Update interval")]

    def __init__(self, text_list: list[str], **config) -> None:
        self.text_list = text_list
        self.text_index = 0
        super().__init__("", **config)
        self.add_defaults(AnimatedText.defaults)

    def poll(self) -> str:
        text = self.text_list[self.text_index]

        if self.text_index == len(self.text_list) - 1:
            self.text_index = 0
        else:
            self.text_index += 1

        return text

