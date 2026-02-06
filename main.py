from src.scripts.dataloader import Dataloader
from src.game.entities.classes.item import Item
from src.game.entities.classes.rarity import Rarity
from src.tools.ui_tools.color_tool import ColorTool

from assets.art.ui.widget import Widget

CT = ColorTool()
W = Widget()

def color_tool_test():
    print(Rarity(1).text_normal('Common'))
    print(Rarity(2).text_bold('Uncommon'))
    print(Rarity(3).text_block('Rare'))
    print(Rarity(4).text_normal('Exotic'))
    print(Rarity(5).text_normal('Legendary'))
    print(f"{CT.effect_bold()}{Rarity(1).text_normal('COMMON')}{CT.clense()}")
    print(f"{CT.effect_dim()}{Rarity(2).text_normal('UNCOMMON')}{CT.clense()}")
    print(f"{CT.effect_underline()}{Rarity(3).text_normal('RARE')}{CT.clense()}")
    print(f"{CT.effect_blink()}{Rarity(4).text_normal('EXOTIC')}{CT.clense()}")
    print(f"{CT.effect_reverse_color()}{Rarity(5).text_normal('LEGENDARY')}{CT.clense()}")
    print(f'{CT.effect_bold()}HELLO{CT.clense()}')
    print(f'{CT.effect_dim()}HELLO{CT.clense()}')
    print(f'{CT.effect_underline()}HELLO{CT.clense()}')
    print(f'{CT.effect_blink()}HELLO{CT.clense()}')
    print(f'{CT.effect_reverse_color()}HELLO{CT.clense()}')
    print(f'{CT.effect_hide()}HELLO{CT.clense()}')


def widget_test():
    print(W.toggle_button(f"{Rarity(5).text_bold('LEGENDARY')}", True))
    print(W.toggle_button(f"{Rarity(5).text_bold('LEGENDARY')}", False))
    print(W.toggle_text(f"{Rarity(3).text_bold('RARE')}", True))
    print(W.toggle_text(f"{Rarity(2).text_bold('UNCOMMON')}", False))


def dataload_test():
    DL = Dataloader()
    item_data = DL.load_item_data()
    print(item_data)
    item = Item(item_data['placeholder_items']['placeholder_ram'])
    print(item.display_item_window())



if __name__ == '__main__':
    # color_tool_test()
    # widget_test()
    dataload_test()
    click = input()
