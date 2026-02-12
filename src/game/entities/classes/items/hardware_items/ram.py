from src.game.entities.classes.items.item import Item

class Ram(Item):
    """
    ram item. here there will be functionality of specific the ram
    """
    def __init__(self, item_data):
        Item.__init__(self, item_data)

        # stats
        self.stats = item_data['stats']


