import random

from src.game.entities.items.Item import Item


class LootGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_loot_from_table(loot_table, item_data):
        loot_list = []
        for loot_data in loot_table:
            if loot_data['chance'] == 1:
                loot_list.append(Item(item_data[loot_data['item']]))
            else:
                for _ in range(0, loot_data['max']):
                    if random.random() <= loot_data['chance']:
                        loot_list.append(Item(item_data[loot_data['item']]))
        return loot_list

