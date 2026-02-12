from data.config.GAME_SETTINGS import WINDOW_LENGTH
from assets.art.ui.widgets.line import Line
from assets.art.ui.widgets.stat_bar import StatBar
from assets.art.ui.widgets.options import Options_menu
from assets.art.ui.config.COLOR_MAP import COLOR_MAP
from assets.art.ui.config.SYMBOL_CONFIG import CURRENCY_SYMBOL
from src.tools.ui_tools.color_tool import ColorTool

CT = ColorTool()
line = Line()
Cmap = COLOR_MAP.copy()

class ItemWindow:

    def __init__(self, Item):
        self.Item = Item


    def full_display(self):

        title = f"{self.Item.Rarity.name} {self.Item.subtype[1]} {self.Item.type[1]}"
        title = f"{title:<40}"
        value_currency = f"{CURRENCY_SYMBOL} {self.Item.value}"
        value_currency = f"{value_currency:<9}"

        string = f"""{line.normal_line()}
{self.Item.Rarity.text_block(f'  {title} {" " * (WINDOW_LENGTH-52)}{value_currency}')} 
    
    {CT.text_rgb_to_ansi(COLOR_MAP['white'])}{CT.effect_bold()}{self.Item.name.upper()}{CT.clense()}
        
{line.small_dark_line()} 
        
        
    {CT.text_rgb_to_ansi(COLOR_MAP['gray1'])}{self.Item.description}{CT.clense()}
        
        
{line.small_dark_line()}  
        
{StatBar().build_item_stat_bar(self.Item)}
        
{line.small_dark_line()}  

{Options_menu().build_options_menu(self.Item)}
          
{line.normal_line(thickness=3)}
"""
        return string

