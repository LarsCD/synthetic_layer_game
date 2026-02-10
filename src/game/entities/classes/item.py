from src.game.entities.classes.rarity import Rarity
from assets.art.ui.windows.item_window import ItemWindow

class Item:
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
        self.options = item_data['options']

        # rarity
        self.Rarity = Rarity(item_data['rarity_value'])

        # value
        self.value = item_data['value']

    def display_item_window(self):
        print(self.full_display)
