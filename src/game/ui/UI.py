from assets.art.ui.windows.textualize_item_window import ItemWindow
from src.game.entities.classes.item import Item         # this might cause loop problems, remove this line if that occurs (07/02/2026)


class UI:
    def __init__(self):
        pass

    def show_item(self, item: Item):
        return ItemWindow(item)
