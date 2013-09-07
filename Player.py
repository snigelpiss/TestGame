import Items
import os


class Inventory:
    def __init__(self, name):
        self.inv = {} # This is the players inventory that we are going to fill with data

    def get_save_path(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "Saves/%s.txt" % self.name
        abs_file_path = os.path.join(script_dir, rel_path)
        return abs_file_path

    def add_item(self, item):
        for k, v in Items.items.items():
            if v['Name'] == item:
                self.inv[len(self.inv)] = v

    def load_inventory(self):
        file = open(self.get_save_path(), "wb+")
        data = file.read()
        split = data.split(',')
        for i in split:
            self.add_item(i)

    def save_inventory(self):
        file = open(self.get_save_path(), "w")
        for k, v in self.inv.items():
            file.write("%s," % v['Name'])

class Player(Inventory):
    def __init__(self, name):
        Inventory.__init__(self, name)
        self.name = name




