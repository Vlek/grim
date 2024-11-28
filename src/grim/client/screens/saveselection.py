from textual import events, on
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, OptionList, Static


class SaveSelectionScreen(Screen):

    CSS = """
    Screen {
        align: center middle;
    }

    OptionList {
        align: center middle;
        width: 70%;
        height: 80%;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("Select save:", id="title")
        yield OptionList("New Game")
        yield Button("Back", id="back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id

        match button_id:
            case "back":
                self.app.push_screen("start")

    @on(OptionList.OptionSelected)
    def save_selected(self, event: OptionList.OptionSelected) -> None:
        option_id = event.option_index
        optionList = event.option_list
        selectedSave: str = optionList.get_option_at_index(option_id).id or ""

        self.app.push_screen("game")

    def on_mount(self) -> None:
        self.query_one(OptionList).focus()
