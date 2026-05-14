from src.core.util.loaders.dataloader import Dataloader
from src.game.systems.level.LevelNode import LevelNode
from src.game.ui.windows.node_password_puzzle_window import NodePasswordPuzzleWindow

DL = Dataloader()


def puzzle_test():
    global DL
    node_data = DL.load_node_data()['placeholder_nodes']
    node = LevelNode(node_data['test_node_1'])

    node.start_puzzle()

    window = NodePasswordPuzzleWindow(node, node.Puzzle)

    # ── Initial render ────────────────────────────────────────────────────────
    print(window.full_display())

    # ── Game loop ─────────────────────────────────────────────────────────────
    while not node.Puzzle.player_has_completed and not node.Puzzle.player_has_failed:
        player_input = input("")   # prompt is rendered inside the window itself

        node.Puzzle.player_tries_password(player_input)

        # ── Pick the right render for the current state ───────────────────────
        if node.Puzzle.player_has_completed:
            print(window.solved_display())
        elif node.Puzzle.player_has_failed:
            print(window.failed_display())
        else:
            correct = node.Puzzle.password_match_list.count(1)
            total   = len(node.Puzzle.password_match_list)
            msg     = f"  ▶  {correct} / {total} characters confirmed  —  {node.Puzzle.tries_left} attempt(s) remaining"
            print(window.attempt_display(player_input, msg))

    input("\n  [ press ENTER to continue ]")


if __name__ == '__main__':
    puzzle_test()