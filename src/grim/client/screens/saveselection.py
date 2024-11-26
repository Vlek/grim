from textual import events
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, Static


class SaveSelectionScreen(Screen):

    def compose(self) -> ComposeResult:
        yield Static("Select save:")
