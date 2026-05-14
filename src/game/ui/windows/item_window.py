from src.game.config.GAME_CONFIG import WINDOW_LENGTH
from src.game.ui.widgets.line import Line
from src.game.ui.widgets.stat_bar import StatBar
from src.game.ui.widgets.options import Options_menu
from src.game.ui.config.COLOR_MAP import COLOR_MAP
from src.game.ui.config.SYMBOL_CONFIG import CURRENCY_SYMBOL
from src.game.ui.tools.color_tool import ColorTool

CT = ColorTool()
line = Line()
Cmap = COLOR_MAP.copy()

class ItemWindow:

    def __init__(self, Item):
        self.Item = Item


    def full_display(self):

        title = f"{self.Item.item_symbol}  │ {self.Item.Rarity.name} {self.Item.subtype[1]} [{self.Item.type[1]}]"
        title = f"{title:<40}"
        value_currency = f"{CURRENCY_SYMBOL} {self.Item.value}"
        value_currency = f"{value_currency:<9}"

        CT.clear_screen()

        string = f"""{self.Item.Rarity.text_block(f'  {title} {" " * (WINDOW_LENGTH-52)}{value_currency}')} 
    
    {CT.text_rgb_to_ansi(COLOR_MAP['white'])}{CT.effect_bold()}{self.Item.name.upper()}{CT.clense()}
        
{line.small_dark_line()} 
        
        
    {CT.text_rgb_to_ansi(COLOR_MAP['gray1'])}{self.Item.description}{CT.clense()}
        
        
{line.small_dark_line()}  
        
{StatBar().build_item_stat_bar(self.Item)}
        
{line.small_dark_line()}  

{Options_menu().build_options_menu(self.Item)}
          
{self.Item.Rarity.text_block(line.normal_line(thickness=1))}
"""
        return string

