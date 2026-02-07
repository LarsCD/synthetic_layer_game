from textual.app import App

from assets.art.ui.windows.textualize_item_window import ItemWindow
from src.game.entities.classes.item import Item
from src.game.ui.UI import UI
from src.scripts.dataloader import Dataloader

DL = Dataloader()
UI_ = UI()
item_data = DL.load_item_data()
item01 = Item(item_data['placeholder_items']['placeholder_firewall01'])

class TestApp(App):
    def on_mount(self):
        self.mount(UI_.show_item(item01))

if __name__ == "__main__":
    TestApp().run()
