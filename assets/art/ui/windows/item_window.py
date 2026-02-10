from data.config.GAME_SETTINGS import WINDOW_LENGTH
from assets.art.ui.widgets.Line import Line
from assets.art.ui.widgets.Stat_bar import StatBar
from data.config.COLOR_MAP import COLOR_MAP
from src.tools.ui_tools.color_tool import ColorTool

CT = ColorTool()
line = Line()
SB = StatBar()
Cmap = COLOR_MAP.copy()

class ItemWindow:

    def __init__(self, Item):
        self.Item = Item


    def full_display(self):

        # stat_bar_building
        stat_bars = SB.build_item_stat_bar(self.Item)


        string = f"""{line.normal_line()}
{self.Item.Rarity.text_block(f'  {self.Item.Rarity.name} {self.Item.type[1]} {" " * (WINDOW_LENGTH-50)}Δ{self.Item.value}')} 
    
{CT.text_rgb_to_ansi(COLOR_MAP['white'])}{CT.effect_bold()}{self.Item.name.upper()}{CT.clense()}
    
{line.small_dark_line()} 
    
    
{CT.text_rgb_to_ansi(COLOR_MAP['gray1'])}{self.Item.description}{CT.clense()}
    
    
{line.small_dark_line()}  
    
{stat_bars}
    
{line.small_dark_line()}  
      
{line.normal_line(thickness=3)}
"""
        return string

