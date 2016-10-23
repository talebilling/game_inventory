"""
Game Inventory by Emese Billing, Oct 2016
"""
import os 

def push_to_inv(key, value):
    if key in inventory:
        inventory[key] += value
    else: 
        inventory[key] = value

def add_to_inventory(inv, added_items):
    for item in added_items:
        push_to_inv(item, 1)

def import_inventory(filename="import_inventory.csv"):
    import_file = open(dir_path + "/" + filename, "r+")
    imported_lines = import_file.readlines()
    import_file.close()
    inv_to_merge = convert_to_inv(imported_lines)
    merge_to_inventory(inv_to_merge)

def convert_to_inv(imported_lines):
    imported_lines = imported_lines[1:]
    imported_lines = [i.split(",") for i in imported_lines]
    new_inv = dict(imported_lines)
    for key, value in new_inv.items():
        new_inv[key] = int(value.strip())
    return new_inv

def merge_to_inventory(inv_to_merge):  
    for key, value in inv_to_merge.items():
        push_to_inv(key, value)
    
def export_inventory(filename="export_inventory.csv"):
    export_file = open(dir_path + "/" + filename, "w+")
    export_lines = create_export_lines()
    export_file.writelines(export_lines)
    export_file.close() 

def create_export_lines():
    first_line_to_export = "item_name,count\n"
    export_lines = [first_line_to_export]
    for key, value in inventory.items():
        export_lines.append(key + "," + str(value) + "\n")
    return export_lines

def display_inventory():
    print("\nInventory: ")
    for key, value in inventory.items():
        print("{} {}" .format(value, key))
    print_num_of_inv_items()
    
def print_num_of_inv_items():
    total_number_of_items = sum(inventory.values())
    print("Total number of items:", total_number_of_items, "\n")

def print_table(order=None):
    inventory_items = sort_inventory_items_by(order)
    key_width = 5 + len(max(inventory.keys(), key=len))
    value_width = 5 + len(str(max(inventory.values())))
    print("\nInventory: ")
    print("{} {}" .format("count".rjust(value_width), "item name".rjust(key_width)))
    print("-" * (key_width + value_width + 1))
    for key, value in inventory_items:
        value = str(value)
        print("{} {}" .format(value.rjust(value_width), key.rjust(key_width)))
    print("-" * (key_width + value_width + 1))
    print_num_of_inv_items()

def sort_inventory_items_by(order):
    sorted_items = inventory.items()
    if order == "count,asc":
        sorted_items = sorted(inventory.items(), key = lambda item: item[1])
    elif order == "count,desc":
        sorted_items = sorted(inventory.items(), key = lambda item: item[1], reverse=True)
    elif order == "item name,asc":
        sorted_items = sorted(inventory.items(), key = lambda item: item[0])
    elif order == "item name,desc":
        sorted_items = sorted(inventory.items(), key = lambda item: item[0], reverse=True)
    return sorted_items

def demo():
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    filename = "inventory_file.csv"
    display_inventory()
    add_to_inventory(inventory, dragon_loot) 
    display_inventory()
    export_inventory(filename)
    import_inventory(filename)
    display_inventory()
    print_table("count,desc")

#definitions
inventory = {'rope': 1, 
            'torch': 6, 
            'gold coin': 42, 
            'dagger': 1, 
            'arrow': 12}
dir_path = os.path.dirname(os.path.realpath(__file__))

demo()