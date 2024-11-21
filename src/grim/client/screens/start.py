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
        width: auto;
        height: auto;
    }
    Vertical {
        width: auto;
        height: auto;
        align: center middle;
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
