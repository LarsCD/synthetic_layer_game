from src.game.ui.windows.item_window import ItemWindow as ItemWindow
from src.game.entities.items.item import Item         # this might cause loop problems, remove this line if that occurs (07/02/2026)


class UI:
    def __init__(self):
        pass

    def get_item_show(self, item: Item):
        return ItemWindow(item).full_display()

