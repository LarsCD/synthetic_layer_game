from src.game.ui.elements.rarity import Rarity
from src.game.ui.elements.option import Option
from src.game.ui.windows.item_window import ItemWindow

class Item:
    """
    Item class, used as blueprint for all item characteristics and function
    """
    def __init__(self, item_data):
        # description
        self.tag = item_data['tag']
        self.name = item_data['name']
        self.description = item_data['description']
        self.type = item_data['type']
        self.subtype = item_data['subtype']

        self.full_display = ItemWindow(self)

        # stats
        self.stats = item_data['stats']

        # options
        self.options = []

        for option in item_data['options']:
            self.options.append(Option(option))

        # rarity
        self.Rarity = Rarity(item_data['rarity_value'])

        # value
        self.value = item_data['value']

    def get_item_window(self):
        return self.full_display
