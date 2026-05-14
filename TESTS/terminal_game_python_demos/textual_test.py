from textual.app import App, ComposeResult
from textual.widgets import Static, Input
from textual.containers import Container
from textual.reactive import reactive
from textual import events


GAME_W = 80
GAME_H = 25


class GameScreen(Static):

    player_x = reactive(40)
    player_y = reactive(12)

    def render(self):

        grid = [[" " for _ in range(GAME_W)] for _ in range(GAME_H)]

        grid[self.player_y][self.player_x] = "@"

        lines = []
        for row in grid:
            lines.append("".join(row))

        return "\n".join(lines)


class GameApp(App):

    CSS = """
    Screen {
        align: center middle;
    }

    #game_container {
        width: 80;
        height: 25;
        border: heavy green;
    }

    #game_view {
        width: 100%;
        height: 100%;
    }

    Input {
        dock: bottom;
        height: 3;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:

        self.game = GameScreen(id="game_view")
        self.input = Input(placeholder="Command input")

        yield Container(self.game, id="game_container")
        yield self.input

    def on_key(self, event: events.Key):

        if self.input.has_focus:
            return

        if event.key == "up":
            self.game.player_y = max(0, self.game.player_y - 1)

        elif event.key == "down":
            self.game.player_y = min(GAME_H - 1, self.game.player_y + 1)

        elif event.key == "left":
            self.game.player_x = max(0, self.game.player_x - 1)

        elif event.key == "right":
            self.game.player_x = min(GAME_W - 1, self.game.player_x + 1)

        self.game.refresh()

    def on_mount(self):
        self.set_focus(self.game)


if __name__ == "__main__":
    GameApp().run()