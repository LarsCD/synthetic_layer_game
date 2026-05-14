from src.core.util.loaders.dataloader import Dataloader
from src.game.entities.items.Inventory import Inventory
from src.game.entities.items.Item import Item
from src.game.ui.windows.textual_inventory_window import InventoryApp

DL = Dataloader()


def test_inventory():

    item_data = DL.load_item_data()['placeholder_items']

    inventory = Inventory()

    item_3 = Item(item_data['placeholder_firewall01'])
    item_2 = Item(item_data['placeholder_cpu'])
    item_1 = Item(item_data['placeholder_ram'])

    inventory.add_item(item_2)

    InventoryApp(inventory).run()


if __name__ == "__main__":
    test_inventory()