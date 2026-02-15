from colorist import ColorRGB, BgColorRGB

from src.game.ui.tools.clear_console import clear_term


class ColorTool:
    def __init__(self):
        pass

    def clense(self):
        return '\x1b[0m'

    def effect_bold(self):
        return '\x1b[1m'

    def effect_dim(self):
        return '\x1b[2m'

    def effect_underline(self):
        return '\x1b[4m'

    def effect_blink(self):
        return '\x1b[5m'

    def effect_reverse_color(self):
        return '\x1b[7m'

    def effect_hide(self):
        return '\x1b[8m'

    def clear_screen(self):
        clear_term()


    def text_rgb_to_ansi(self, rgb_tuple: tuple):
        return ColorRGB(rgb_tuple[0], rgb_tuple[1], rgb_tuple[2])
        # if TypeError here, probably wrong rarity id (not 1-5)

    def background_rgb_to_ansi(self, rgb_tuple: tuple):
        return BgColorRGB(rgb_tuple[0], rgb_tuple[1], rgb_tuple[2])
