from src.game.ui.config.CORRUPTION_EFFECT_SYMBOLS import CORRUPTION_EFFECT_SYMBOLS, EXCLUSION_CHARACTER_LIST

import re
import random

ANSI_PATTERN = re.compile(r'\x1b\[[0-?]*[ -/]*[@-~]')

class Corrupt:
    def __init__(self, exclusion_chars=None, corruption_symbols=None):
        pass

    def apply(self, text, corruption_percentage=0.25):
        """
        Processes strings containing ANSI escape sequences without breaking them.
        Only visible characters are subject to corruption.
        """
        parts = ANSI_PATTERN.split(text)
        ansi_tokens = ANSI_PATTERN.findall(text)

        result = []

        for i, part in enumerate(parts):
            # Corrupt only visible text
            corrupted_part = ''.join(
                c if c in EXCLUSION_CHARACTER_LIST or random.random() >= corruption_percentage
                else random.choice(CORRUPTION_EFFECT_SYMBOLS)
                for c in part
            )
            result.append(corrupted_part)

            # Reinsert ANSI token if present
            if i < len(ansi_tokens):
                result.append(ansi_tokens[i])

        return ''.join(result)
