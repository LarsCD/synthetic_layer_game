from assets.art.ui.windows.item_window import ItemWindow as ItemWindow
from assets.art.ui.windows.textualize_item_window import ItemWindow as ItemWindow2
from src.game.entities.classes.item import Item         # this might cause loop problems, remove this line if that occurs (07/02/2026)


class UI:
    def __init__(self):
        pass

    def get_item_show(self, item: Item):
        return ItemWindow(item).full_display()

    def get_item_show2(self, item: Item):
        return ItemWindow2(item).full_display()
