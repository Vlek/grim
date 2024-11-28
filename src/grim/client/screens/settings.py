from textual import events, on
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, OptionList, Static


class SettingsScreen(Screen):

    def compose(self) -> ComposeResult:
        yield Static("Settings options:")
