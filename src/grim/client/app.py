from textual.app import App

from grim import GrimConfig

from .screens import GameScreen, SaveSelectionScreen, SettingsScreen, StartScreen


class GrimApp(App):
    CSS = """
    Screen {
        align: center middle;
        width: auto;
        height: auto;
    }
    VerticalGroup {
        width: auto;
        height: auto;
        border: solid red;
        content-align: center middle;
    }
    #title {
        align: center top;
        width: auto;
        height: auto;
    }
    """

    def __init__(self, config: GrimConfig) -> None:
        self.config = config
        super().__init__()

    SCREENS = {
        "start": StartScreen,
        "saveselection": SaveSelectionScreen,
        "game": GameScreen,
        "settings": SettingsScreen,
    }

    def on_mount(self) -> None:
        self.push_screen("start")
