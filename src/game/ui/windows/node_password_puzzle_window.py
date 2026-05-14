from src.game.ui.config.COLOR_MAP import COLOR_MAP
from src.game.ui.tools.color_tool import ColorTool
from src.game.ui.widgets.line import Line
from src.game.config.GAME_CONFIG import WINDOW_LENGTH

CT = ColorTool()
line = Line()


# ── Symbol constants ──────────────────────────────────────────────────────────
SYM_BLOCK     = '█'
SYM_LIGHT     = '░'
SYM_DOT       = '·'
SYM_ARROW     = '▶'
SYM_BULLET    = '◆'
SYM_CORNER_TL = '╔'
SYM_CORNER_TR = '╗'
SYM_CORNER_BL = '╚'
SYM_CORNER_BR = '╝'
SYM_HORIZ     = '═'
SYM_VERT      = '║'
SYM_T_LEFT    = '╠'
SYM_T_RIGHT   = '╣'


class NodePasswordPuzzleWindow:
    """
    Terminal UI window for the PasswordPuzzle mini-game.

    Usage
    -----
        window = NodePasswordPuzzleWindow(node, puzzle)
        print(window.full_display())

        # after each attempt:
        print(window.attempt_display(player_input, result_msg))

        # on completion:
        print(window.solved_display())
        print(window.failed_display())
    """

    # ── Colour aliases ────────────────────────────────────────────────────────
    _C_TITLE   = "highlight_green"
    _C_DIM     = "dark_grey"
    _C_WARN    = "yellow"
    _C_DANGER  = "red"
    _C_SUCCESS = "highlight_green"
    _C_NEUTRAL = "white"

    # ── Layout ────────────────────────────────────────────────────────────────
    _GAUGE_WIDTH = 20

    def __init__(self, node, puzzle):
        self.node   = node
        self.puzzle = puzzle

    # ═════════════════════════════════════════════════════════════════════════
    #  PUBLIC API
    # ═════════════════════════════════════════════════════════════════════════

    def full_display(self, status_msg: str = '') -> str:
        CT.clear_screen()
        return self._build_window(status_msg)

    def attempt_display(self, player_input: str, result_msg: str = '') -> str:
        CT.clear_screen()
        return self._build_window(result_msg)

    def solved_display(self) -> str:
        CT.clear_screen()
        return self._build_window(self._solved_banner())

    def failed_display(self) -> str:
        CT.clear_screen()
        return self._build_window(self._failed_banner())

    # ═════════════════════════════════════════════════════════════════════════
    #  PRIVATE – WINDOW ASSEMBLY
    # ═════════════════════════════════════════════════════════════════════════

    def _build_window(self, status_msg: str = '') -> str:
        parts = [
            self._top_border(),
            self._node_header(),
            self._divider(),
            self._password_section(),
            self._divider(),
            self._tries_section(),
            self._divider(),
            self._status_section(status_msg),
            self._hint_section(),
            self._bottom_border(),
            self._input_prompt(),
        ]
        return '\n'.join(parts)

    # ─── Borders ─────────────────────────────────────────────────────────────

    def _top_border(self) -> str:
        inner = SYM_HORIZ * (WINDOW_LENGTH - 2)
        return self._colour(f"  {SYM_CORNER_TL}{inner}{SYM_CORNER_TR}", self._C_TITLE)

    def _bottom_border(self) -> str:
        inner = SYM_HORIZ * (WINDOW_LENGTH - 2)
        return self._colour(f"  {SYM_CORNER_BL}{inner}{SYM_CORNER_BR}", self._C_TITLE)

    def _divider(self) -> str:
        inner = SYM_HORIZ * (WINDOW_LENGTH - 2)
        return '\n' + self._colour(f"  {SYM_T_LEFT}{inner}{SYM_T_RIGHT}", self._C_DIM) + '\n'

    def _vert(self) -> str:
        """Left border pipe + indent. No right-side pipe — avoids ANSI width misalignment."""
        return f"  {self._colour(SYM_VERT, self._C_TITLE)}   "

    # ─── Node header ─────────────────────────────────────────────────────────

    def _node_header(self) -> str:
        n = self.node

        title_row = (
            f"{self._vert()}"
            f"{self._colour(f'{SYM_BULLET} PASSWORD DECRYPTION PUZZLE {SYM_BULLET}', self._C_TITLE)}"
        )

        row1 = (
            f"{self._vert()}"
            f"{self._colour('TAG', self._C_DIM)}: {self._colour(n.tag.upper(), self._C_TITLE)}   "
            f"{self._colour('NODE', self._C_DIM)}: {self._colour(n.name.upper(), self._C_NEUTRAL)}   "
            f"{self._colour('TYPE', self._C_DIM)}: {self._colour(n.type.upper(), self._C_WARN)}"
        )

        row2 = (
            f"{self._vert()}"
            f"{self._colour('DIFFICULTY', self._C_DIM)}: {self._difficulty_pips(n.difficulty)}"
        )

        return '\n'.join(['', title_row, row1, row2, ''])

    def _difficulty_pips(self, level: int) -> str:
        filled = self._colour(SYM_BLOCK * level,       self._C_DANGER)
        empty  = self._colour(SYM_LIGHT * (5 - level), self._C_DIM)
        label  = self._colour(f'  [{level}/5]',        self._C_DIM)
        return filled + empty + label

    # ─── Password section ─────────────────────────────────────────────────────

    def _password_section(self) -> str:
        show_list  = self.puzzle.password_show_list
        match_list = self.puzzle.password_match_list

        header       = f"{self._vert()}{self._colour('DECRYPT  —  CHARACTER SLOTS', self._C_DIM)}"
        progress_row = f"{self._vert()}{self._build_progress_bar(match_list)}"

        if not show_list:
            slots_row = f"{self._vert()}{self._colour('(puzzle not initialised)', self._C_DIM)}"
        else:
            slots_row = f"{self._vert()}{self._build_slot_row(show_list, match_list)}"

        return '\n'.join(['', header, slots_row, '', progress_row, ''])

    def _build_slot_row(self, show_list, match_list) -> str:
        sep   = self._colour(f'  {SYM_DOT}  ', self._C_DIM)
        cells = []
        for i, char in enumerate(show_list):
            matched = (match_list[i] == 1) if i < len(match_list) else False
            if matched:
                cell = self._colour(f'[{char}]', self._C_SUCCESS)
            else:
                cell = (
                    f"{CT.effect_blink()}"
                    f"{self._colour(f'[{char}]', self._C_DANGER)}"
                    f"{CT.clense()}"
                )
            cells.append(cell)
        return sep.join(cells)

    def _build_progress_bar(self, match_list) -> str:
        if not match_list:
            return ''
        total   = len(match_list)
        correct = match_list.count(1)
        filled  = int((correct / total) * self._GAUGE_WIDTH)
        empty   = self._GAUGE_WIDTH - filled

        bar   = self._colour(SYM_BLOCK * filled,  self._C_SUCCESS) + self._colour(SYM_LIGHT * empty, self._C_DIM)
        label = self._colour('PROGRESS', self._C_DIM)
        count = self._colour(f'  {correct}/{total} chars', self._C_DIM)

        return f"{label}  [{bar}]{count}"

    # ─── Tries section ────────────────────────────────────────────────────────

    def _tries_section(self) -> str:
        left  = self.puzzle.tries_left
        total = self.puzzle.tries

        header = f"{self._vert()}{self._colour('ATTEMPTS REMAINING', self._C_DIM)}"
        gauge  = f"{self._vert()}{self._build_tries_gauge(left, total)}"

        return '\n'.join(['', header, gauge, ''])

    def _build_tries_gauge(self, left: int, total: int) -> str:
        if left > total * 0.6:
            colour = self._C_SUCCESS
        elif left > total * 0.3:
            colour = self._C_WARN
        else:
            colour = self._C_DANGER

        pips_on  = self._colour((SYM_BLOCK + '  ') * left,           colour)
        pips_off = self._colour((SYM_LIGHT + '  ') * (total - left),  self._C_DIM)
        count    = self._colour(f'  {left}/{total}', colour)

        return f"[{pips_on}{pips_off}]{count}"

    # ─── Status section ───────────────────────────────────────────────────────

    def _status_section(self, msg: str = '') -> str:
        if not msg:
            if self.puzzle.player_has_completed:
                msg = self._solved_banner()
            elif self.puzzle.player_has_failed:
                msg = self._failed_banner()
            elif self.puzzle.player_has_started:
                msg = self._colour('▶  Awaiting input...', self._C_DIM)
            else:
                msg = self._colour('▶  Puzzle ready.', self._C_DIM)

        header = f"{self._vert()}{self._colour('STATUS', self._C_DIM)}"
        row    = f"{self._vert()}{msg}"

        return '\n'.join(['', header, row, ''])

    def _solved_banner(self) -> str:
        return (
            f"{CT.effect_bold()}"
            f"{self._colour('✓  ACCESS GRANTED  —  NODE DECRYPTED', self._C_SUCCESS)}"
            f"{CT.clense()}"
        )

    def _failed_banner(self) -> str:
        return (
            f"{CT.effect_blink()}"
            f"{CT.effect_bold()}"
            f"{self._colour('✗  ACCESS DENIED  —  LOCKOUT TRIGGERED', self._C_DANGER)}"
            f"{CT.clense()}"
        )

    # ─── Hint section ─────────────────────────────────────────────────────────

    def _hint_section(self) -> str:
        hint = self._colour(
            f'{SYM_DOT}  Enter one character per position. Correct guesses are locked in.',
            self._C_DIM
        )
        return f"\n{self._vert()}{hint}\n"

    # ─── Input prompt ─────────────────────────────────────────────────────────

    def _input_prompt(self) -> str:
        if self.puzzle.player_has_completed or self.puzzle.player_has_failed:
            return ''
        arrow  = self._colour(SYM_ARROW, self._C_TITLE)
        prompt = self._colour(' ENTER PASSWORD: ', self._C_NEUTRAL)
        return f'\n  {arrow}{prompt}'

    # ─── Colour helper ────────────────────────────────────────────────────────

    def _colour(self, text: str, colour_key: str) -> str:
        try:
            rgb = COLOR_MAP[colour_key]
            return f'{CT.text_rgb_to_ansi(rgb)}{text}{CT.clense()}'
        except (KeyError, AttributeError):
            return text
