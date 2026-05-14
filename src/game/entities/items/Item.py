import logging

from src.core.util.logger.dev_logger import DevLogger
from src.game.ui.config.COLOR_MAP import COLOR_MAP
from src.game.ui.elements.Rarity import Rarity
from src.game.ui.elements.Option import Option
from src.game.ui.renderer.effect.corrupt import Corrupt
from src.game.ui.tools.color_tool import ColorTool
from src.game.ui.tools.get_item_symbol import get_item_symbol
from src.game.ui.windows.item_window import ItemWindow

CT = ColorTool()

class Item:
    """
    Item class, used as blueprint for all item characteristics and function
    """
    def __init__(self, item_data):
        # logger
        self.log = DevLogger(Item).log

        # indexing info
        self.tag = item_data['tag']                             # name of .json name            ("placeholder_ram")
        self.name = item_data['name']                           # display name                  ("Placeholder RAM")
        self.type = item_data['type']                           # type of item                  (["hardware", "Hardware"])
        self.subtype = item_data['subtype']                     # subtype of item               (["ram", "RAM Module"])

        # general item data
        self.description = item_data['description']             # description of item           ("Random Access Memory, ...")
        self.Rarity = Rarity(item_data['rarity_value'])         # rarity (or tier) of item      (Rarity type (class))
        self.value = item_data['value']                         # value of item                 (1200)
        self.stats = item_data['stats']                         # list of stats of item         ({"size": 4.0, "speed": 20.0})
        self.quantity = 0                                       # how many of this item         (1)

        self.item_symbol = get_item_symbol(self.type)

        # option functionality
        self.options = []

        for option in item_data['options']:
            self.options.append(Option(option))                 # options for in item View      (Option type (class))

        # UI
        self.full_display = ItemWindow(self)                    # full display string of View   (String type)

        # flags
        self.is_stackable = item_data['is_stackable']           # item can have more of itself  (True)
        self.is_equipped = False                                # if item is equipped right now (False)
        self.is_indexable = True

# ========== QUANTITY FUNCTIONALITY ==========

    def sell(self):
        self.log(logging.INFO, f'SELLING \'{self.tag}\' ({self})')
        if 'sell' in self.options:
            # sell the item
            # functionality will be added after markets (name tbd) is implemented
            pass

# ========== QUANTITY FUNCTIONALITY (DISCONTINUED SINCE v0.2.0) ==========
#     def update_quantity(self):
#         if not self.is_stackable:
#             if self.quantity > 1:
#                 self.log(logging.WARNING, f'\'{self.tag}\' is not stackable, setting quantity to 1 ({self})')
#                 self.quantity = 1
#         if self.quantity < 0:
#             self.quantity = 0
#         if self.quantity == 0:
#             self.destroy()
#
#     def add_quantity(self, quantity):
#         if self.is_stackable:
#             self.log(logging.INFO, f'ADDED \'{self.tag}\' (+{quantity}) ({self})')
#             self.quantity += quantity
#             self.update_quantity()
#         else:
#             self.log(logging.WARNING, f'CANNOT ADD: is_stackable={self.is_stackable} \'{self.tag}\' (+{quantity}) ({self})')
#
#     def remove_quantity(self, quantity):
#         if self.is_stackable:
#             self.log(logging.WARNING, f'REMOVING \'{self.tag}\' (-{quantity}) ({self})')
#             self.quantity -= quantity
#             self.update_quantity()
#         else:
#             self.log(logging.WARNING, f'CANNOT REMOVE : is_stackable={self.is_stackable} \'{self.tag}\' (-{quantity}) ({self})')
#
#     def set_quantity(self, quantity):
#         self.log(logging.INFO, f'SET \'{self.tag}\' (:{quantity}) ({self})')
#         self.quantity = quantity
#         self.update_quantity()

    def destroy(self):
        self.log(logging.INFO, f'DESTROYING \'{self.tag}\' ({self})')
        del self


# ========== UI ELEMENTS ==========
    def View(self):
        self.log(logging.INFO, f'VIEWING \'{self.tag}\' ({self})')
        print(self.full_display.full_display())

    def getView(self):
        self.log(logging.INFO, f'GET VIEW \'{self.tag}\' ({self})')
        return self.full_display.full_display()

    def getOneLinerDisplay(self, show_name=True, show_rarity=True, name_corruption=0.0, is_encrypted=False):

        title = '?????'
        rarity = ''
        symbol = ''

        encrypted = ''
        if is_encrypted:
            encrypted = f'{CT.effect_blink()}{CT.effect_bold()}{CT.text_rgb_to_ansi(COLOR_MAP["red"])}// ENCRYPTED //{CT.clense()}'

        if show_rarity:
            rarity = f"[{self.Rarity.text_bold(self.Rarity.name)}]"
            symbol = f"{self.Rarity.text_bold(self.item_symbol)}"
        else:
            rarity = ''
            symbol = self.item_symbol

        if show_name:
            title = f"{symbol}  {CT.text_rgb_to_ansi(COLOR_MAP['white'])}{CT.effect_bold()}{self.name}{CT.clense()}"

        if name_corruption is not None:
            title = f"{Corrupt().apply(title, corruption_percentage=name_corruption)}"
        if show_rarity:
            return f'{self.Rarity.text_bold(f"{title}")}{CT.clense()} {rarity}'
        else:
            return f'{CT.text_rgb_to_ansi(COLOR_MAP["white"])}{title}{CT.clense()} {rarity}'

