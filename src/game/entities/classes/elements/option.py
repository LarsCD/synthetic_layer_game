from assets.art.ui.config.COLOR_MAP import COLOR_MAP

class Option:
    def __init__(self, option_data):

        self.name = option_data['name']
        self.color = COLOR_MAP[option_data['color']]

        # flags & functionality
        self.index: int = 0  # used for indexing option for input

        self.is_available = True  # will be grayed out if not
        self.is_selected = False

        # ui flags
        self.has_tab = False


    def get_option_element(self):
        return

