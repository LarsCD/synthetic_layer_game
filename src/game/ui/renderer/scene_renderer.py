import sys
import time
import re

from src.core.util.helpers.usleep import usleep
from src.game.systems.dialogue.Scene import Scene
from src.game.systems.dialogue.scene_choice_manager import ChoiceManager
from src.game.ui.config.COLOR_MAP import COLOR_MAP
from src.game.ui.renderer.effect.corrupt import Corrupt
from src.game.ui.tools.color_tool import ColorTool
from src.game.ui.widgets.options import Options_menu

CT = ColorTool()


class SceneRenderer:
    def __init__(self):
        self.default_type_speed = 100
        self.type_speed = self.default_type_speed

        self.color_pattern = re.compile(r"<:(\w+)>|<:clr>")


    def render_scene(self, scene: Scene):
        self.scene_handler(scene)


    def scene_handler(self, scene: Scene):
        # made with ChatGPT because this shit gave me headaches, but it works...

        current_tag_index = 0
        while current_tag_index is not None and current_tag_index < len(scene.dialogue_node_tags):
            current_tag = scene.dialogue_node_tags[current_tag_index]
            dialogue_nodes = scene.dialogue_nodes[current_tag]

            next_tag = None
            for dialogue_node in dialogue_nodes:
                result = self.node_handler(dialogue_node)
                if result and 'function' in result:
                    if result['function'] == 'next':
                        if result['next'] in scene.dialogue_nodes:
                            next_tag = result['next']
                        else:
                            next_tag = None
                    elif result['function'] == 'exit':
                        return  # stop the scene immediately

            if next_tag is not None:
                current_tag_index = scene.dialogue_node_tags.index(next_tag)
            else:
                current_tag_index = None


    def node_handler(self, dialogue_node):
        if dialogue_node['type'] == 'scene_text':
            self.render_text_node(dialogue_node)
            return None
        if dialogue_node['type'] == 'choice_text':
            self.render_options_node(dialogue_node)
            player_choice = self.get_choice(dialogue_node)
            if player_choice['function'] == 'next':
                return player_choice
        return None


    def render_text_node(self, dialogue_node):
        self.write(*dialogue_node.values())


    def render_options_node(self, dialogue_node):
        self.write(*dialogue_node.values())


    def get_choice(self, dialogue_node):
        if dialogue_node['choices'] is not None:
            player_choice = ChoiceManager().choose(dialogue_node['choices'])
            return player_choice


    def check_message_has_valid_color_pattern(self, message):
        stack = []

        for match in self.color_pattern.finditer(message):
            tag = match.group(1)

            if tag == "clr":
                if not stack:
                    return False
                stack.pop()
            else:
                if tag not in COLOR_MAP:
                    return False
                stack.append(tag)

        return len(stack) == 0

    def message_apply_coloring(self, message):
        if not self.check_message_has_valid_color_pattern(message):
            return message

        def repl(match):
            tag = match.group(1)

            if tag == "clr":
                return str(CT.clense())

            rgb = COLOR_MAP.get(tag)
            if not rgb:
                return ""

            return str(CT.text_rgb_to_ansi(rgb))

        return self.color_pattern.sub(repl, message)

    def write(self,
              type,
              message,
              sender,
              color,
              show_sender,
              text_speed,
              newline,
              end_time_buffer,
              effects,
              option,
              function
              ):

        if text_speed is not None:
            self.type_speed = text_speed

        if show_sender and sender:
            print(f'\n[{CT.text_rgb_to_ansi(COLOR_MAP[color])}{sender}{CT.clense()}]')

        if effects is not None:
            if 'corruption_percentage' in effects:
                message = Corrupt().apply(message, effects['corruption_percentage'])

        message = self.message_apply_coloring(message)

        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()

            # Adjust timing based on character
            if char in {',', '.', ';', ':', '!', '?'}:
                if type == 'scene_text':
                    time.sleep(0.4)
            elif char == '\n':
                if type == 'scene_text':
                    time.sleep(0.6)
            else:
                if type == 'scene_text':
                    time.sleep(1 / self.type_speed)
                else:
                    usleep(250)

        # Add buffer delay at the end
        time.sleep(end_time_buffer)

        # Reset to default typing speed
        self.type_speed = self.default_type_speed


        # Print newline if required
        if newline:
            print()

