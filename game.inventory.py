"""
Game Inventory
"""

def display_inventory(inv):
    item_numbers = list(inv.values())
    total_number_of_items = sum(item_numbers) 

    print("\nInventory: ")
    for k, v in inv.items():
        print("{} {}" .format(v, k))
    print("Total number of items:", total_number_of_items, "\n")

def add_to_inventory(inv, added_items):
    for item in added_items:
        if inv.get(item):
            inv[item] += 1
        else:
            inv.update({item : 1})
    return inv

def import_inventory(filename, lines): #but by default it's "import_inventory.csv"
    database = open(filename, "r+")
    lines = database.readlines()
    lines = lines[1:]

    #split strings
    lines = [i.split("\n")[0] for i in lines if "\n" in i]
    print(lines)
    database.close()
    return lines

#main
#definitions
inventory = {'rope': 1, 
            'torch': 6, 
            'gold coin': 42, 
            'dagger': 1, 
            'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
filename = "input_file.csv"
lines = []

inventory = add_to_inventory(inventory, dragon_loot) #add items to inv.
display_inventory(inventory) #printing out the inventory
lines = import_inventory(filename, lines)
inventory = add_to_inventory(inventory, lines)
display_inventory(inventory)