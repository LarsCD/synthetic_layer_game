from src.game.ui.config.COLOR_MAP import COLOR_MAP
from src.game.ui.elements.Option import Option
from src.game.ui.tools.color_tool import ColorTool
from src.game.config.GAME_CONFIG import TAB_WIDTH

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

    def build_scene_choice_menu(self, choices, give_tab=False):
        # shit code here we go!! (12-2-2026)
        # never look at this again, just make it work and call it a day...
        if choices is not None:
            options = []
            for selection in choices:
                option_data = {
                    'name': selection['text'],
                    'color': 'white'
                }
                options.append(Option(option_data))

            options_menu = ''

            for i, option in enumerate(options):
                option.index = i + 1
                options_menu += self.option_custom(
                    option,
                    give_tab=give_tab
                )

            return options_menu
        return None


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
