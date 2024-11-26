from textual import events
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, Static

logo: str = r"""
  ________       __         
 /  _____/______|__| _____  
/   \  __\_  __ \  |/     \ 
\    \_\  \  | \/  |  Y Y  \
 \______  /__|  |__|__|_|  /
        \/               \/ 
"""


class StartScreen(Screen):
    CSS = """
    Screen {
        align: center middle;
        width: 100%;
        height: 100%;
    }
    #title {
        align: center top;
        width: auto;
        height: auto;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static(logo, id="title")

        with Vertical():
            yield Button("Play", id="play")
            yield Button("Quit", id="quit")

    def on_key(self, event: events.Key) -> None:
        match event.key:
            case "j":
                self.focus_next()
            case "k":
                self.focus_previous()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id

        match button_id:
            case "play":
                self.app.push_screen("saveselection")
            case "quit":
                self.app.exit("Goodbye, thanks for playing.")
