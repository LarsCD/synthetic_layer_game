import random

from traits.trait_types import self

from src.game.systems.puzzles.PUZZLE_CONFIG import PUZZLE_PASSWORD_INFILL_CHAR


class PasswordPuzzle:
    def __init__(self, node_data):
        self.node_data = node_data

        # puzzle password variables
        self.password = ''

        self.password_as_list = []
        self.password_match_list = []
        self.password_show_list = []

        self.missing_characters = 0

        self.tries = node_data['tries']
        self.tries_left = self.tries


        # flags
        self.player_has_started = False
        self.player_has_ended = False
        self.player_has_completed = False
        self.player_has_failed = False


# ===== GAMEPLAY MECHANICS =====
    def player_tries_password(self, player_input):
        self.match_player_input_to_password(player_input)
        self.update_show_list()
        self.update_puzzle()
        self.DEBUG_print_show_list()


    def match_player_input_to_password(self, player_input):
        # remove rest of player input if longer then password
        if len(player_input) > len(self.password_as_list):
            player_input = player_input[:len(self.password_as_list)]
            print(f'password is too long, only checking: {list(player_input)}')

        for i, char in enumerate(player_input):
            if char.lower() == self.password_as_list[i].lower():
                self.password_match_list[i] = 1


    def update_missing_in_password(self):
        self.missing_characters = self.password_match_list.count(0)


    def check_if_complete(self):
        if self.missing_characters == 0:
            return True


# ===== UI MECHANICS =====
    def get_show_list(self):
        return self.password_show_list

    def DEBUG_print_show_list(self):
        print(self.password_show_list)


# ===== PUZZLE MECHANICS =====
    def init_puzzle(self):
        self.player_has_started = True
        self.password = random.choice(self.node_data['pass_list'])
        self.fill_password_as_list()
        self.reset_match_list()
        self.update_missing_in_password()


    def update_puzzle(self):
        self.update_missing_in_password()

        if self.check_if_complete() == True:
            self.player_has_completed = True
            print('PUZZLE IS SOLVED!!!')


    def fill_password_as_list(self):
        for char in self.password:
            self.password_as_list.append(char)


    def reset_match_list(self):
        self.password_match_list = []
        for _ in self.password:
            self.password_match_list.append(0)


    def update_show_list(self):
        self.password_show_list = self.password_as_list.copy()
        for i, char in enumerate(self.password_as_list):
            if self.password_match_list[i] == 1:
                pass
            else:
                self.password_show_list[i] = PUZZLE_PASSWORD_INFILL_CHAR


    def reset_tries(self):
        self.tries_left = self.tries


    def reset_flags(self):
        self.player_has_started = False
        self.player_has_ended = False
        self.player_has_completed = False
        self.player_has_failed = False


    # reset puzzle should be a universal method in all future puzzle classes
    def reset_puzzle(self):
        self.reset_hidden_list()
        self.reset_tries()
        self.reset_flags()


    def restart_puzzle(self):
        self.reset_puzzle()
        self.init_puzzle()

