class RarityStyle:
    def __init__(self, rarity_obj):
        self.name = rarity_obj.name
        self.rgb = rarity_obj.primary_color_rgb

    def color(self):
        r, g, b = self.rgb
        return f"rgb({r},{g},{b})"
