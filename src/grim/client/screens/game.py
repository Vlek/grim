from datetime import datetime

from textual import events, on
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, Input, OptionList, RichLog, Static, Tabs


class GameScreen(Screen):

    CSS = """
    Tabs {
        dock: top;
    }
    #gamelog {
        margin: 1 2;
    }
    #gameinput {
        dock: bottom;
    }
    """

    def compose(self) -> ComposeResult:
        self.gameLog = RichLog(wrap=True, id="gamelog")
        self.gameInput = Input(id="gameinput")

        yield Tabs("Log", "Inventory", "Character", "Quests", "Notes")
        yield self.gameLog
        yield self.gameInput

    def on_mount(self) -> None:
        self.gameInput.focus()

    @on(Input.Submitted)
    def submit_input(self, event: Input.Submitted) -> None:
        self.gameInput.clear()

        timestamp: str = datetime.now().strftime("%I:%M:%S")
        self.gameLog.write(f"[{timestamp}]: {event.value}")
