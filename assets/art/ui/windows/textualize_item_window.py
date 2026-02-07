from textual.widget import Widget
from rich.text import Text
from rich.panel import Panel
from rich.rule import Rule
from rich.console import Group

from src.tools.ui_tools.rarity_style import RarityStyle


class ItemWindow(Widget):
    def __init__(self, Item, window_length=80):
        super().__init__()
        self.Item = Item
        self.window_length = window_length
        self.rarity = RarityStyle(self.Item.Rarity)

    def render(self):
        color = self.rarity.color()

        # HEADER BLOCK (rarity bar)
        header_text = f"  {self.rarity.name} {self.Item.subtype[1]} [{self.Item.type[1]}]"
        value_text = f"Δ{self.Item.value}"
        spacing = " " * max(1, self.window_length - len(header_text) - len(value_text) - 4)

        header = Text(
            header_text + spacing + value_text,
            style=f"bold {color} reverse"
        )

        # NAME
        name = Text(self.Item.name.upper(), style="bold white")

        # DESCRIPTION
        description = Text(self.Item.description, style="rgb(150,150,150)")

        # STATS
        stats = Text(f"Stats: {self.Item.stats}", style="rgb(120,120,120)")

        # OPTIONS
        options = Text(" | ".join(self.Item.options), style="dim")

        # COMPOSE WINDOW
        return Panel(
            Group(
                header,
                "",
                name,
                Rule(style="rgb(80,80,80)"),
                description,
                Rule(style="rgb(80,80,80)"),
                stats,
                "",
                options
            ),
            border_style=color,
            width=self.window_length
        )
