from src.game.config.GAME_CONFIG import WINDOW_LENGTH, TAB_WIDTH
from src.game.entities.items.config.ITEM_CONFIG import ITEM_STAT_CONFIG
from src.game.ui.config.SYMBOL_CONFIG import INCREASE_SYMBOL, DECREASE_SYMBOL
from src.game.ui.tools.color_tool import ColorTool

CT = ColorTool()


class StatBar:
    RESET = "\033[0m"
    FG_LIGHT = "\033[38;2;188;188;188m"
    FG_DARK = "\033[38;2;42;42;42m"
    FG_GREEN = "\033[38;2;29;236;138m"
    FG_RED = "\033[38;2;218;3;80m"

    def build_item_stat_bar(self, item):
        result = []
        subtype_config = ITEM_STAT_CONFIG[item.subtype[0]]

        for stat, value in item.stats.items():
            config = subtype_config.get(stat)

            if config is None:
                result.append(f"{stat.replace('_', ' ').title()} {value}\n")
                continue

            result.append(
                self.stat_bar(
                    name=stat.replace("_", " ").title(),
                    value=value,
                    MIN_STAT=config["min"],
                    MAX_STAT=config["max"],
                    BAR_WIDTH=WINDOW_LENGTH - 50,
                    unit=config["unit"],
                    old_value=20,
                    show_minmax=False,
                    is_inverted=config["inverted"],
                    give_tab=True,
                )
                + "\n"
            )

        return "".join(result)

    def stat_bar(
        self,
        name,
        value,
        MIN_STAT=0,
        MAX_STAT=100,
        BAR_WIDTH=20,
        unit=None,
        old_value=None,
        character="▬",
        show_minmax=False,
        is_inverted=False,
        give_tab=False,
    ):
        def normalize(v):
            n = (v - MIN_STAT) / (MAX_STAT - MIN_STAT)
            n = max(0.0, min(1.0, n))
            return 1.0 - n if is_inverted else n

        norm = normalize(value)
        filled = int(norm * BAR_WIDTH)

        old_filled = None
        if old_value is not None:
            old_norm = normalize(old_value)
            old_filled = int(old_norm * BAR_WIDTH)

        improved = None
        if old_value is not None:
            improved = (value < old_value) if is_inverted else (value > old_value)

        bar_chars = []

        delta_indices = set()
        if old_filled is not None and old_filled != filled:
            start = min(filled, old_filled)
            end = max(filled, old_filled)

            if start == end:
                delta_indices.add(start)
            else:
                for i in range(start, end):
                    delta_indices.add(i)

            if not delta_indices:
                delta_indices.add(min(filled, BAR_WIDTH - 1))

        for i in range(BAR_WIDTH):
            if i < filled:
                if i in delta_indices and improved is not None:
                    color = self.FG_GREEN if improved else self.FG_RED
                else:
                    color = self.FG_LIGHT
                bar_chars.append(f"{color}{character}")
            else:
                if i in delta_indices and improved is not None:
                    color = self.FG_GREEN if improved else self.FG_RED
                    bar_chars.append(f"{color}{character}")
                else:
                    bar_chars.append(f"{self.FG_DARK}{character}")

        if delta_indices and improved is not None:
            if len(delta_indices) == 1:
                idx = next(iter(delta_indices))
                if 0 <= idx < BAR_WIDTH:
                    color = self.FG_GREEN if improved else self.FG_RED
                    bar_chars[idx] = f"{color}{character}"

        bar = "".join(bar_chars) + self.RESET

        unit_label = unit or ""
        tab = " " * TAB_WIDTH if give_tab else ""

        delta_str = ""
        if old_value is not None:
            delta = round(value - old_value, 1)
            if delta != 0:
                positive = delta > 0
                effective_positive = positive ^ is_inverted
                color = self.FG_GREEN if effective_positive else self.FG_RED
                symbol = INCREASE_SYMBOL if positive else DECREASE_SYMBOL
                if is_inverted:
                    symbol = DECREASE_SYMBOL if positive else INCREASE_SYMBOL
                sign = "+" if positive else "-"
                delta_str = (
                    f" {CT.effect_bold()}{color}{sign}{abs(delta)}{CT.clense()} "
                    f"{unit_label} {color}{symbol}{CT.clense()}"
                )

        minmax = f"[{value}/{MAX_STAT}]" if show_minmax else ""
        label = f"{name:<15} "
        spacing = " " * max(0, BAR_WIDTH - 30)

        return (
            f"{tab}{label} {minmax} {spacing}{value} {unit_label} {delta_str}\n"
            f"{tab}{bar}"
        )


if __name__ == "__main__":
    panel = StatBar()
    print(panel.stat_bar("Health", 5, MAX_STAT=25, BAR_WIDTH=60, old_value=20))
    print(panel.stat_bar("Mana", 40, BAR_WIDTH=60, old_value=60))
    print(panel.stat_bar("Stamina", 90, BAR_WIDTH=60))
    input()