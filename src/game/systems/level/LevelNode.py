from src.game.systems.puzzles.passwords import PasswordPuzzle


class LevelNode:
    def __init__(self, node_data):
        self.node_data = node_data

        self.tag = node_data['tag']
        self.name = node_data['name']
        self.type = node_data['type']

        self.difficulty = node_data['difficulty']

        # puzzle
        self.Puzzle = None


    def start_puzzle(self):
        self.puzzle_manager()


    def puzzle_manager(self):
        if self.type == 'passwords':
            self.init_passwords_puzzle()


    def init_passwords_puzzle(self):
        self.Puzzle = PasswordPuzzle(self.node_data)
        self.Puzzle.init_puzzle()


    def reset_node(self):
        self.Puzzle.reset_puzzle()


    def restart_node(self):
        self.Puzzle.restart_puzzle()

