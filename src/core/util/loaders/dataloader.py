import logging
import os
import json
from pprint import pprint

from src.core.util.loaders.config.DATALOADER_CONFIG import ITEM_FOLDER_PATH
from src.core.util.logger.dev_logger import DevLogger
from src.core.util.helpers.find_root import find_root


class Dataloader:
    """
    Class used to load data from folders
    """
    def __init__(self):
        self.log = DevLogger(Dataloader).log
        self.cwd = find_root()

        self.item_dir_path = {
            'item_dir': ITEM_FOLDER_PATH,
        }

    def load_item_data(self):
        """
        Load all the items present in the item_dir_path
        """
        full_path = f"{self.cwd}{self.item_dir_path['item_dir']}"
        self.log(logging.INFO, f'loading items data ({self.item_dir_path["item_dir"]})')

        data_list = self.load_data_from_path(full_path)
        return data_list


    def load_data_from_path(self, full_path):
        """
        Load all the items present in a specific full_path
        """
        data_list = {}
        for filename in os.listdir(full_path):
            if filename.endswith(".json"):
                file_path = os.path.join(full_path, filename)
                self.log(logging.INFO, f'loading \'{filename}\'')
                with open(file_path, "r") as file:
                    loaded_data = json.load(file)
                    data_list[filename.removesuffix('.json')] = loaded_data
        return data_list


if __name__ == '__main__':
    data = Dataloader().load_item_data()
    pprint(data)
