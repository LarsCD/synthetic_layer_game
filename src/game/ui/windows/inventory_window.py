from src.game.config.GAME_CONFIG import WINDOW_LENGTH
from src.game.ui.widgets.inventory_list_builder import InventoryLister
from src.game.ui.widgets.line import Line
from src.game.ui.widgets.stat_bar import StatBar
from src.game.ui.widgets.options import Options_menu
from src.game.ui.config.COLOR_MAP import COLOR_MAP
from src.game.ui.config.SYMBOL_CONFIG import CURRENCY_SYMBOL
from src.game.ui.tools.color_tool import ColorTool

CT = ColorTool()
line = Line()


class InventoryWindow:
    def __init__(self, Inventory):
        self.Inventory = Inventory

    def full_display(self):
        title = f"    {str(self.Inventory.get_parent_name()).upper()} INVENTORY"

        count = ''
        encrypted = ''
        if self.Inventory.is_encrypted:
            encrypted = f'         {CT.effect_blink()}{CT.effect_bold()}{CT.text_rgb_to_ansi(COLOR_MAP["red"])}// ENCRYPTED //{CT.clense()}'

        item_count = self.Inventory.get_item_count()
        max_item_count = self.Inventory.size_limit

        green = CT.text_rgb_to_ansi(COLOR_MAP["highlight_green"])

        if max_item_count is None:
            count = f'{CT.text_rgb_to_ansi(COLOR_MAP["highlight_green"])}{item_count}{CT.clense()} items'
        elif self.Inventory.is_encrypted:
            count = f'         {CT.effect_blink()}{CT.effect_bold()}{CT.text_rgb_to_ansi(COLOR_MAP["red"])}// NO PERMISSION //{CT.clense()}'
        else:
            percentage = round(item_count / max_item_count * 100)
            count = f'{green}{item_count}{CT.clense()}/{green}{max_item_count}{CT.clense()} ({green}{percentage}%{CT.clense()})'


        inventory_list = InventoryLister().build_inventory_index_list(self.Inventory, self.Inventory.show_item_names, self.Inventory.show_item_rarity, self.Inventory.name_corruption)

        if self.Inventory.is_encrypted:
            inventory_list = f'             {CT.effect_blink()}{CT.effect_bold()}{CT.text_rgb_to_ansi(COLOR_MAP["red"])}// CONTENTS IS NOT AVAILABLE //{CT.clense()}'

        CT.clear_screen()
        string = f"""{self.Inventory.Rarity.text_block(f'{title} {" " * (WINDOW_LENGTH-len(title))}')}
        
    {encrypted}
    
    {count}
    
{line.small_dark_line(indent=True)}

{inventory_list}

{line.normal_line(thickness=3)}
"""
        return string



