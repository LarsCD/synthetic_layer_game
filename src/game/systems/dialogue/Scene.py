

class Scene:
    def __init__(self, scene_data):
        self.tag = [key for key, val in scene_data.items()][0]

        scene_dialogue_nodes = scene_data[self.tag]
        self.dialogue_node_tags = [node_tag for node_tag, val in scene_dialogue_nodes.items()]
        self.dialogue_nodes = scene_data[self.tag]
        print(self.dialogue_nodes)
        print(self.dialogue_node_tags)