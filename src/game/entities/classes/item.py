from src.game.entities.classes.rarity import Rarity
from assets.art.ui.windows.item_window import full_display

class Item:
    def __init__(self, item_data):
        # description
        self.tag = ['tag']
        self.name = item_data['name']
        self.description = item_data['description']
        self.type = item_data['type']

        # rarity
        self.Rarity = Rarity(item_data['rarity_value'])

        # value
        self.value = item_data['value']

    def display_item_window(self):
        print(full_display(self))
