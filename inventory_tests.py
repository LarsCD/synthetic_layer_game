from src.core.util.loaders.dataloader import Dataloader
from src.game.entities.items.Inventory import Inventory
from src.game.entities.items.Item import Item
from src.game.entities.items.hardware_items.Ram import RamHardware

DL = Dataloader()



def test_inventory():
    # setup
    global DL
    item_data = DL.load_item_data()['placeholder_items']
    inventory = Inventory()
    item_4 = Item(item_data['placeholder_firewall02'])
    item_3 = Item(item_data['placeholder_firewall01'])
    item_2 = Item(item_data['placeholder_cpu'])
    item_1 = Item(item_data['placeholder_ram'])

    # ADD AND REMOVE
    print('\nADD AND REMOVE\n')
    print(inventory.get_all_item_tags())

    inventory.add_item(item_1)
    inventory.add_item(item_2)
    print(inventory.get_all_item_tags())


    inventory.remove_item(item_1.tag)
    print(inventory.get_all_item_tags())

    # SORT
    print('\nSORT\n')
    inventory.add_items_as_list([item_1, item_2, item_3, item_4])
    inventory.get_all_item_tags()

    inventory.sort_on_rarity()
    print(inventory.get_all_item_tags())

    inventory.sort_on_rarity(reverse=True)
    # inventory.show_item_rarity = False
    inventory.show_item_names = True
    inventory.name_corruption = 0
    print(inventory.get_all_item_tags())

    # SHOW
    print('\nSHOW\n')

    print(inventory.View())
    input('> ENCRYPT')

    inventory.turn_encrypted()
    print(inventory.View())
    input('> EXIT')


if __name__ == '__main__':
    # tests
    test_inventory()
