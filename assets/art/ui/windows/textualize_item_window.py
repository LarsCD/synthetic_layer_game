from textual.widget import Widget
from rich.text import Text
from rich.panel import Panel
from rich.rule import Rule
from rich.console import Group

from src.tools.ui_tools.rarity_style import RarityStyle


class ItemWindow(Widget):
    """UI widget that renders an item panel in Textual."""

    def __init__(self, item, width: int = 80):
        super().__init__()
        self.item = item
        self.width = width
        self.rarity = RarityStyle(item.Rarity)

    def render(self):
        color = self.rarity.color()

        # ---------- HEADER BAR ----------
        header_left = f" {self.rarity.name} {self.item.subtype[1]} [{self.item.type[1]}] "
        header_right = f"Δ{self.item.value} "
        padding = max(1, self.width - len(header_left) - len(header_right) - 4)
        header_text = header_left + (" " * padding) + header_right

        header = Text(header_text, style=f"bold {color} reverse")

        # ---------- BODY CONTENT ----------
        name = Text(self.item.name.upper(), style="bold white")
        description = Text(self.item.description, style="rgb(150,150,150)")
        stats = Text(f"Stats: {self.item.stats}", style="rgb(120,120,120)")
        options = Text(" | ".join(self.item.options), style="dim")

        # ---------- FOOTER BAR ----------
        bottom_bar = Text("▓" * (self.width - 4), style=color)

        # ---------- COMPOSE PANEL ----------
        return Panel(
            Group(
                header,
                "",                       # spacer line
                name,
                Rule(style="rgb(80,80,80)"),
                description,
                Rule(style="rgb(80,80,80)"),
                stats,
                "",
                options,
                "",
                bottom_bar,
            ),
            border_style=color,
            width=self.width,
        )
