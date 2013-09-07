import Player

# An example on how you can run your code

ply = Player.Player("Timothy") # Create a player who's name is Timothy

ply.load_inventory() # Load Timothy's inventory from a text file (Empty if it's the first run)

for i in range(0,1000000):
    ply.add_item('Sword') # Add 1 million swords to his inventory

ply.save_inventory() # Save Timothy's inventory to the text file called Timothy