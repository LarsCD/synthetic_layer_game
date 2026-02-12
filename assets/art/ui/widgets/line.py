from assets.art.ui.config.COLOR_MAP import COLOR_MAP
from data.config.GAME_SETTINGS import *
from src.tools.ui_tools.color_tool import ColorTool

CT = ColorTool()

class Line:
    def __init__(self):
        pass

    def normal_line(self, thickness=4) -> str:
        """
        Character line with '░', '▒', '▓', '█' thickness character of length WINDOW_LENGTH
        :thickness: the thickness of the character (index 1-4)
        """

        char = ['░', '▒', '▓', '█']

        return char[thickness-1] * WINDOW_LENGTH


    def box_line(self):
        """
        Character line with '═' thickness character of length WINDOW_LENGTH
        """
        return '═' * WINDOW_LENGTH


    def small_dark_line(self, indent=True):
        if indent:
            return f"    {CT.text_rgb_to_ansi(COLOR_MAP['gray3'])}{'─' * (WINDOW_LENGTH - 8)}{CT.clense()}"
        else:
            return f"{CT.text_rgb_to_ansi(COLOR_MAP['gray3'])}{'─' * WINDOW_LENGTH}{CT.clense()}"
