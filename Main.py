import Player

ply = Player.Player("Test")

ply.load_inventory()

ply.add_unique_item('Sword')

for k, v in ply.inv.items():
    print v

ply.save_inventory()



