"""
Game Inventory
by Emese Billing, Oct 2016
"""

def add_to_inventory(inv, added_items):
    for item in added_items:
        if inv.get(item):
            inv[item] += 1
        else:
            inv.update({item : 1})
    display_inventory(inv)
    return inv

def import_inventory(filename="import_inventory.csv"):
    database = open(filename, "r+")
    item_list = database.readlines()
    database.close()
    split_strings(inventory, item_list)

def split_strings(inv, item_list):
    item_list = item_list[1:]
    item_list = [i.split("\n")[0] for i in item_list if "\n" in i]
    item_list = [i.split(",", 1) for i in item_list if "," in i]
    print(item_list)
    ##should change the values to int
    item_dic = dict(item_list)
    return inv, item_list

def display_inventory(inv):
    item_numbers = list(inv.values())
    total_number_of_items = sum(item_numbers) 
    #print Inventory
    print("\nInventory: ")
    for k, v in inv.items():
        print("{} {}" .format(v, k))
    print("Total number of items:", total_number_of_items, "\n")

#main
#definitions
inventory = {'rope': 1, 
            'torch': 6, 
            'gold coin': 42, 
            'dagger': 1, 
            'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
filename = "input_file.csv"

#add items to inventory
inventory = add_to_inventory(inventory, dragon_loot) 
display_inventory(inventory) #printing out the inventory
