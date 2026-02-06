from src.game.entities.classes.item import Item

class Ram(Item):
    def __init__(self, item_data):
        Item.__init__(self, item_data)

        # stats
        self.stats = item_data['stats']


