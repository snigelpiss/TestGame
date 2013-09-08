import Player

ply = Player.Player("Timss")

ply.load_inventory()

ply.add_unique_item('Sword')

for k, v in ply.inv.items():
    print v

ply.save_inventory()



