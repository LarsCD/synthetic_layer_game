from src.game.entities.items.Inventory import Inventory


class Player(Inventory):
    """
   Player class, used as blueprint for all player characteristics and function
   """
    def __init__(self):
        # info
        super().__init__()

        self.tag = 'player'
        self.name = 'Player'




