from src.game.ui.renderer.actions.typewiter import Typewrite
from src.game.ui.widgets.options import Options_menu


class ChoiceManager:
    def __init__(self):
        pass

    def choose(self, choices):
        print('')
        self.print_choice(choices)
        player_choice = self.player_input(choices)
        return player_choice

    def print_choice(self, choices):
        TW = Typewrite()
        TW.write(Options_menu().build_scene_choice_menu(choices))

    def player_input(self, choices):
        while True:
            player_input = input('> ')
            for i, _ in enumerate(choices):
                index = i+1
                if player_input == str(index):
                    player_choice = choices[i]
                    return player_choice
