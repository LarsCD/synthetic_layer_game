from src.scripts.dataloader import Dataloader
from src.game.entities.classes.items.item import Item
from src.game.entities.classes.elements.rarity import Rarity
from src.tools.ui_tools.color_tool import ColorTool
from src.game.ui.UI import UI

from assets.art.ui.widgets.button import Button

CT = ColorTool()
B = Button()

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
    print(B.toggle_button(f"{Rarity(5).text_bold('LEGENDARY')}", True))
    print(B.toggle_button(f"{Rarity(5).text_bold('LEGENDARY')}", False))
    print(B.toggle_text(f"{Rarity(3).text_bold('RARE')}", True))
    print(B.toggle_text(f"{Rarity(2).text_bold('UNCOMMON')}", False))


def dataload_test():
    DL = Dataloader()
    ui = UI()
    item_data = DL.load_item_data()
    # print(item_data)
    item1 = Item(item_data['placeholder_items']['placeholder_ram'])
    item2 = Item(item_data['placeholder_items']['placeholder_cpu'])
    item3 = Item(item_data['placeholder_items']['placeholder_firewall01'])
    item4 = Item(item_data['placeholder_items']['placeholder_firewall02'])

    print(ui.get_item_show(item1))
    input()
    print(ui.get_item_show(item2))
    input()
    print(ui.get_item_show(item3))
    input()
    print(ui.get_item_show(item4))
    input()

def test_generated_items_test():
    DL = Dataloader()
    ui = UI()
    item_data = DL.load_item_data()

    for item_tag in item_data['placeholder_items']:
        item = Item(item_data['placeholder_items'][item_tag])
        print(ui.get_item_show(item))
        input()




if __name__ == '__main__':
    # color_tool_test()
    # widget_test()
    # dataload_test()
    test_generated_items_test()

    click = input()
