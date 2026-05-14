import logging

from traits.trait_types import self

from src.core.util.logger.dev_logger import DevLogger
from src.game.entities.items.Item import Item
from src.game.ui.elements.Rarity import Rarity
from src.game.ui.windows.inventory_window import InventoryWindow


class Inventory:
    def __init__(self):
        self.log = DevLogger(Inventory).log

        # content
        self.content_list = []
        self.parent = None
        self.size_limit = 14

        self.rarity_value = 1
        self.Rarity = Rarity(self.rarity_value)

        # flags
            # inventory display
        self.show_item_names = True
        self.show_item_rarity = True
        self.name_corruption = 0
        self.is_encrypted = False

        self.full_display = ''

    def set_parent(self, parent):
        self.parent = parent

    def get_parent_tag(self):
        if self.parent is not None:
            return self.parent.tag
        else:
            return None

    def get_parent_name(self):
        if self.parent is not None:
            return self.parent.name
        else:
            return None

    def add_item(self, Item: Item):
        self.content_list.append(Item)
        self.log(logging.INFO, f'ADDED ITEM {Item.name} to ({self.parent}:{self})')

    def add_items_as_list(self, Items_list: list):
        self.content_list.extend(Items_list)

    def remove_item(self, item_tag):
        for Item in self.content_list:
            if Item.tag == item_tag:
                self.content_list.remove(Item)
                self.log(logging.INFO, f'REMOVED ITEM {Item.name} ({self.parent}:{self})')

    def get_contents(self):
        return self.content_list

    def get_all_item_tags(self):
        list = []

        for Item in self.content_list:
            list.append(Item.tag)

        return list

    def get_item_count(self):
        return len(self.content_list)

    def sort_on_rarity(self, reverse=False):
        self.content_list.sort(key=lambda item: item.Rarity.rarity_value, reverse=reverse)

    def turn_encrypted(self):
        self.is_encrypted = True
        self.show_item_names = False
        self.show_item_rarity = False

    def updateView(self):
        self.full_display = InventoryWindow(self).full_display()

    def View(self):
        self.updateView()
        return self.full_display
