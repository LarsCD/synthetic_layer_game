from src.game.systems.dialogue.Scene import Scene
from src.game.systems.level.LevelNode import LevelNode
from src.game.systems.loot_generator import LootGenerator


class Level:
    def __init__(self, level_data, scene_data, node_data, item_data):
        self.tag = level_data['tag']
        self.name = level_data['name']
        self.difficulty = level_data['difficulty']

        self.scenes = []

        # fill scene list
        for scene_tag in level_data['scenes']:
            self.scenes.append(Scene(scene_data[scene_tag]))

        self.nodes = []

        # fill node list
        for node_tag in level_data['nodes']:
            self.nodes.append(LevelNode(node_data[node_tag]))

        # loot
        self.completion_loot = LootGenerator.generate_loot_from_table(level_data['completion_loot_table'], item_data)
        self.scavenge_loot = LootGenerator.generate_loot_from_table(level_data['scavenge_loot_table'], item_data)

        # flags
        self.loot_is_encrypted = level_data['is_encrypted']          # only used for showing/hiding loot
        self.show_loot_names = level_data['show_loot_names']

    def print_all_loots(self):
        print(self.completion_loot)
        print(self.scavenge_loot)

