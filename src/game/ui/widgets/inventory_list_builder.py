from src.game.ui.config.COLOR_MAP import COLOR_MAP
from src.game.ui.tools.color_tool import ColorTool
from src.game.ui.widgets.line import Line

CT = ColorTool()
line = Line()

class InventoryLister:

    def build_inventory_index_list(self, Inventory,
                        show_name=False,
                        show_rarity=True,
                        name_corruption=None,

                ):
        index_list = ''

        n = 0

        if not Inventory.is_encrypted:

            for i, Item in enumerate(Inventory.get_contents()):
                blank_color = CT.text_rgb_to_ansi(COLOR_MAP['gray1'])
                index_color = ''

                if Item.is_indexable:
                    index_color = CT.text_rgb_to_ansi(COLOR_MAP['highlight_green'])
                else:
                    index_color = blank_color

                index_list += (str(f'    [{index_color}{i + 1:02}{CT.clense()}]: ' + Item.getOneLinerDisplay(
                    show_name=show_name,
                    show_rarity=show_rarity,
                    name_corruption=name_corruption,
                    is_encrypted=Inventory.is_encrypted,
                ) + '\n'))

                n += 1

            # add blank spaces if inventory has size limit
            if Inventory.size_limit:
                for j in range(Inventory.size_limit - n):
                    index_list += f'    {blank_color}[{j + 1 + n:02}]: ---\n'

            return index_list

        else:
            for i, Item in enumerate(Inventory.get_contents()):
                index_color = CT.text_rgb_to_ansi(COLOR_MAP['gray1'])
                index_list += (str(f'    [{index_color}{i + 1:02}{CT.clense()}]: {CT.effect_blink()}{CT.effect_bold()}{CT.text_rgb_to_ansi(COLOR_MAP["red"])}// ERROR //{CT.clense()}\n'))

            return index_list


