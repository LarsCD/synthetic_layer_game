from src.game.ui.config.SYMBOL_CONFIG import HARDWARE_SYMBOL, SOFTWARE_SYMBOL

def get_item_symbol(item_type):
    if item_type[0] == 'hardware':
        return HARDWARE_SYMBOL
    elif item_type[0] == 'software':
        return SOFTWARE_SYMBOL
