from data.config.GAME_SETTINGS import WINDOW_LENGTH
from src.tools.ui_tools.ui_tool import UiTool
from assets.art.color_map import color_map
from src.tools.ui_tools.color_tool import ColorTool

CT = ColorTool()
UIt = UiTool()
Cmap = color_map.copy()

class ItemWindow:
    def __init__(self, Item):
        self.Item = Item

    def full_display(self):
        string = f"""{UIt.normal_line()}
    {self.Item.Rarity.text_block(f'  {self.Item.Rarity.name} {self.Item.type} {" " * (WINDOW_LENGTH-40)}Δ{self.Item.value}')} 
    
    {CT.text_rgb_to_ansi(color_map['white'])}{CT.effect_bold()}{self.Item.name.upper()}{CT.clense()}
    
       {CT.text_rgb_to_ansi(color_map['gray3'])}────────────────────────────────────────────────────{CT.clense()}  
    
    
    {CT.text_rgb_to_ansi(color_map['gray1'])}{self.Item.description}{CT.clense()}
    
    
       {CT.text_rgb_to_ansi(color_map['gray3'])}────────────────────────────────────────────────────{CT.clense()}  
      
    {UIt.normal_line(thickness=3)}
"""
        return string

