from typing import Callable

from textual.widgets import Button


class ActionButton(Button):

    def __init__(self, on_press: Callable) -> None:
        self.on_press = on_press
        super().__init__()

    def on_click(self) -> None:
        self.on_press()
