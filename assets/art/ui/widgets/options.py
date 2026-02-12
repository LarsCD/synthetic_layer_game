from assets.art.ui.config.COLOR_MAP import COLOR_MAP
from data.config.GAME_SETTINGS import TAB_WIDTH
from src.tools.ui_tools.color_tool import ColorTool

CT = ColorTool()

class Options_menu:

    def build_options_menu(self, Item):

        options_menu = ''

        for i, Option in enumerate(Item.options):
            Option.index = i + 1
            options_menu += self.option_custom(
                Option,
                give_tab=True
        )

        return options_menu


    def option_custom(self, Option, give_tab=False):

        grayed_out = ''  # will be default highlighted green if not grayed out
        if not Option.is_available:
            grayed_out = CT.text_rgb_to_ansi(COLOR_MAP['gray1'])

        tab = ''
        if give_tab:
            tab = ' '*TAB_WIDTH

        index_color = CT.text_rgb_to_ansi(COLOR_MAP['highlight_green'])

        string = f"{tab}[{index_color}{grayed_out}{Option.index}{CT.clense()}]: {CT.text_rgb_to_ansi(Option.color)}{grayed_out}{Option.name.upper()}{CT.clense()}\n"
        return string
