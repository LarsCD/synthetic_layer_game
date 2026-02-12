from data.config.GAME_SETTINGS import WINDOW_LENGTH, TAB_WIDTH
from data.config.ITEM_CONFIG import ITEM_STAT_CONFIG
from src.tools.ui_tools.color_tool import ColorTool

CT = ColorTool()


class StatBar:
    RESET = "\033[0m"
    FG_LIGHT = "\033[38;2;188;188;188m"
    FG_DARK = "\033[38;2;42;42;42m"
    FG_GREEN = "\033[38;2;29;236;138m"
    FG_RED = "\033[38;2;218;3;80m"


    def build_item_stat_bar(self, Item):
        stat_build = ""
        for stat in Item.stats:
            if ITEM_STAT_CONFIG[Item.subtype[0]][stat] is None:
                stat_build += f'{stat.replace("_", " ").title()} {Item.stats[stat]}\n'
            else:
                # get max and is inverted from item configuration
                min = ITEM_STAT_CONFIG[Item.subtype[0]][stat]['min']
                max = ITEM_STAT_CONFIG[Item.subtype[0]][stat]['max']
                inverted = ITEM_STAT_CONFIG[Item.subtype[0]][stat]['inverted']
                unit = ITEM_STAT_CONFIG[Item.subtype[0]][stat]['unit']

                # turn stat name into statbar title
                stat_name = stat.replace("_", " ").title()

                if inverted:
                    pass

                # build statbar
                stat_build += self.stat_bar(
                    name=stat_name,
                    value=Item.stats[stat],
                    MIN_STAT=min,
                    MAX_STAT=max,
                    BAR_WIDTH=WINDOW_LENGTH-50,
                    unit=unit,
                    old_value=min,
                    show_minmax=False,
                    give_tab=True
                )
                stat_build += '\n'
        return stat_build

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
            give_tab=False
    ):
        # bar generation
        norm = (value - MIN_STAT) / (MAX_STAT - MIN_STAT)
        norm = max(0.0, min(1.0, norm))

        if is_inverted:
            norm = 1.0 - norm

        filled = int(norm * BAR_WIDTH)
        empty = BAR_WIDTH - filled

        bar = (
            f"{self.FG_LIGHT}{character * filled}"
            f"{self.FG_DARK}{character * empty}"
            f"{self.RESET}"
        )

        # creating delta
        delta_str = ""
        if old_value is not None:
            delta = round(value - old_value, 1)
            if delta != 0:
                positive = delta > 0
                color = self.FG_GREEN if (positive ^ is_inverted) else self.FG_RED
                sign = "+" if positive else "-"
                delta_str = f" {color}{sign}{abs(delta)}{self.RESET}"

        minmax_label = f"[{value}/{MAX_STAT}]" if show_minmax else ""
        unit_label = unit or ""
        tab_space = ""

        label = f"{name:<15} "

        if give_tab:
            tab_space = ' '*TAB_WIDTH

        return f"{tab_space}{label} {minmax_label} {' ' * (BAR_WIDTH - 30)}{value} {unit_label} {delta_str}\n{tab_space}{bar}"


# Example usage
if __name__ == "__main__":
    panel = StatBar()
    print(panel.stat_bar("Health", 75, BAR_WIDTH=60, old_value=30))
    print(panel.stat_bar("Mana", 40, BAR_WIDTH=60, old_value=60))
    print(panel.stat_bar("Stamina", 90, BAR_WIDTH=60))
    input()
