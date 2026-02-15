from src.game.entities.items.item import Item

class Ram(Item):
    """
    Ram item. Used to hold ram module functionality
    """
    def __init__(self, item_data):
        Item.__init__(self, item_data)

        # stats
        self.stats = item_data['stats']


