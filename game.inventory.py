"""
Game Inventory
"""

def display_inventory(inv):
    item_numbers = list(inv.values())
    total_number_of_items = sum(item_numbers)

    print("\nInventory: ")
    for k, v in inv.items():
        print("{} {}" .format(v, k))
    print("Total number of items:", total_number_of_items)

def add_to_inventory(added_items, inv):
    for item in added_items:
        if inv.get(item):
            inv[item] += 1  #print("Value : {}" .format(inventory.get(item)))
        else:
            inv.update({item : 1})
    return inv



#main
#definitions
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} #the player’s inventory, keys = strings, values of items, value = integer (how many of that item)
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
order = 9

inventory = add_to_inventory(dragon_loot, inventory)
display_inventory(inventory) #printing out the inventory