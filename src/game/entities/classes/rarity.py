from data.config.RARITY_DATA import rarity_data_list
from src.tools.ui_tools.color_tool import ColorTool

CT = ColorTool()

class Rarity:
    def __init__(self, rarity_value):
        self.rarity_value = rarity_value

        # data
        self.tag = rarity_data_list[rarity_value]['tag']
        self.name = rarity_data_list[rarity_value]['name']

        # color
        self.primary_color_rgb = rarity_data_list[rarity_value]['primary_color']
        self.secondary_color_rgb = rarity_data_list[rarity_value]['secondary_color']


    def text_normal(self, text):
        return f'{CT.text_rgb_to_ansi(self.primary_color_rgb)}{text}{CT.clense()}'

    def text_bold(self, text):
        return f'{CT.effect_bold()}{CT.text_rgb_to_ansi(self.primary_color_rgb)}{text}{CT.clense()}'

    def text_block(self, text):
        return f'{CT.effect_reverse_color()}{CT.text_rgb_to_ansi(self.primary_color_rgb)}{text}{CT.clense()}'

