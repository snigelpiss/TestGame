import Items
import os
from random import randint
import ast



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

    def add_unique_item(self, item):
        rand_unique = randint(0,len(Items.unique) - 1)
        unique = Items.unique[rand_unique]
        store_item = {}

        for k, v in Items.items.items():
            if v['Name'] == item:
                store_item = dict(v)
                store_item['Name'] = "%s-%s" % (unique['Name'], store_item['Name'])
                for i in unique:
                    if i != 'Name':
                        rand_attr = randint(unique[i][0], unique[i][1])
                        store_item[i] = store_item[i] + rand_attr
                        store_item['Unique'] = 1
        self.inv[len(self.inv)] = store_item

    def separate_unique_attr(self, item):
        split = item.split("^")
        return dict(ast.literal_eval(str(split[2])))

    def load_inventory(self):
        file = open(self.get_save_path(), "r")
        data = file.read()
        split = data.split(',,')
        for i in split:
            for k, v in Items.items.items():
                if i == v['Name']:
                    self.add_item(i)
            if len(data) > 0:
                if i[0] == '^':
                    self.inv[len(self.inv)] = self.separate_unique_attr(i)
        file.close()

    def save_inventory(self):
        file = open(self.get_save_path(), "w")
        for k, v in self.inv.items():
            if k + 1 == len(self.inv) and v['Unique'] == 1:
                file.write("^%s^%s" % (v['Name'], v))
            elif k + 1 == len(self.inv):
                file.write("%s" % v['Name'])
            elif v['Unique'] == 1:
                file.write("^%s^%s,," % (v['Name'], v))
            elif v['Unique'] == 0:
                file.write("%s,," % v['Name'])
        file.close()

class Player(Inventory):
    def __init__(self, name):
        Inventory.__init__(self, name)
        self.name = name