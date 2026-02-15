from src.game.ui.tools.color_tool import ColorTool

CT = ColorTool()

class Button:
    def __init__(self):
        pass

    def toggle_button(self, text, is_active, color='', effect=''):
        if is_active:
            return f"[{CT.effect_bold()}{text}{CT.clense()}]"
        else:
            return f"[{CT.effect_dim()}{text}{CT.clense()}]"

    def toggle_text(self, text, is_active, color='', effect=''):
        if is_active:
            return f"{CT.effect_bold()}{text}{CT.clense()}"
        else:
            return f"{CT.effect_dim()}{text}{CT.clense()}"

