from data.config.GAME_SETTINGS import *

class UiTool:
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

