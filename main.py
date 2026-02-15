import time

from src.core.util.loaders.dataloader import Dataloader
from src.game.ui.renderer.actions.typewiter import Typewrite
from src.game.ui.renderer.effect.corrupt import Corrupt
from src.game.ui.elements.rarity import Rarity
from src.game.ui.tools import clear_console
from src.game.ui.tools.color_tool import ColorTool
from src.game.ui.widgets.button import Button
from src.game.ui.renderer.ui.UI import UI
from src.game.entities.items.item import Item
from assets.scenes.test_scenes.scene1_test import scene_interact


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
    input()

def widget_test():
    print(B.toggle_button(f"{Rarity(5).text_bold('LEGENDARY')}", True))
    print(B.toggle_button(f"{Rarity(5).text_bold('LEGENDARY')}", False))
    print(B.toggle_text(f"{Rarity(3).text_bold('RARE')}", True))
    print(B.toggle_text(f"{Rarity(2).text_bold('UNCOMMON')}", False))
    input()

def dataload_test():
    DL = Dataloader()
    ui = UI()
    item_data = DL.load_item_data()
    # print(item_data)
    item1 = Item(item_data['placeholder_items']['placeholder_ram'])

    input()
    print(ui.get_item_show(item1))
    input()

def test_generated_items_test():
    DL = Dataloader()
    ui = UI()
    item_data = DL.load_item_data()

    for item_tag in item_data['placeholder_items']:
        item = Item(item_data['placeholder_items'][item_tag])
        print(ui.get_item_show(item))
        input()

def test_typewrite_renderer_test():
    CR = Corrupt()
    DL = Dataloader()
    ui = UI()
    TW = Typewrite()
    item_data = DL.load_item_data()
    for item_tag in item_data['placeholder_items']:
        item = Item(item_data['placeholder_items'][item_tag])
        CT.clear_screen()
        TW.write(CR.apply(ui.get_item_show(item), corruption_percentage=0.6))
        input()
    CT.clear_screen()
    TW.scene(scene_interact)

def corruption_test():
    CR = Corrupt()
    p = 0
    while True:
        clear_console.clear_term()
        p += 0.05
        print(CR.apply('Hello, My name is Lars! My passcode is: ABCDE12345', corruption_percentage=p) + f'     corruption_percentage={round(p, 1)}')
        time.sleep(0.1)



if __name__ == '__main__':
    # color_tool_test()
    # widget_test()
    # dataload_test()
    # test_generated_items_test()
    # test_typewrite_renderer_test()
    corruption_test()

    click = input()
