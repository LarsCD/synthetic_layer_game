from src.game.entities.items.Item import Item

class RamHardware(Item):
    """
    Ram item. Used to hold ram module functionality
    """
    def __init__(self, item_data):
        super().__init__(item_data)
