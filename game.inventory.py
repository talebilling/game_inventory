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
    return inv

def import_inventory(filename, item_list): #but by default it's "import_inventory.csv"
    database = open(filename, "r+")
    item_list = database.readlines()
    item_list = item_list[1:]
    #split strings
    item_list = [i.split("\n")[0] for i in item_list if "\n" in i]
    database.close()
    return item_list

def add_inventory_from_import(inv, item_list):
    #convert list to dict
    item_list = [i.split(",", 1) for i in item_list if "," in i]
    ##should change the values to int
    item_dic = dict(item_list)
    #add to inventory
    return inv

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
items_from_file = []

inventory = add_to_inventory(inventory, dragon_loot) #add items to inv.
items_from_file = import_inventory(filename, items_from_file)
add_inventory_from_import(inventory, items_from_file)
display_inventory(inventory) #printing out the inventory
