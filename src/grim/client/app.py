from textual.app import App

from .screens import SaveSelectionScreen, StartScreen


class GrimApp(App):
    CSS = """
    Screen {
        align: center middle;
        width: auto;
        height: auto;
    }
    Vertical {
        width: auto;
        height: auto;
    }
    #title {
        align: center top;
        width: auto;
        height: auto;
    }
    """

    SCREENS = {"start": StartScreen, "saveselection": SaveSelectionScreen}

    def on_mount(self) -> None:
        self.push_screen("start")
