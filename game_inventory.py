"""
Game Inventory
by Emese Billing, Oct 2016
"""
import os 

def add_to_inventory(inv, added_items):
    for item in added_items:
        if inv.get(item):
            inv[item] += 1
        else:
            inv.update({item : 1})

def import_inventory(filename="import_inventory.csv"):
    database = open(dir_path + "/" + filename, "r+")
    item_list = database.readlines()
    database.close()
    inv_to_merge = split_strings(item_list)
    merge_to_inventory(inv_to_merge)

def split_strings(item_list):
    item_list = item_list[1:]
    item_list = [i.split(",") for i in item_list]
    item_dic = dict(item_list)
    dictionary_keys_list = item_dic.keys()
    for dic_key in dictionary_keys_list:
        value = item_dic.get(dic_key)
        value = int(value.strip())
        item_dic[dic_key] = value
    return item_dic

def merge_to_inventory(inv_to_merge):
    dictionary_keys_list = inv_to_merge.keys()    
    for dic_key in dictionary_keys_list:
        if inventory.get(dic_key):
            inventory[dic_key] += inv_to_merge[dic_key]
        else: 
            inventory.update({dic_key : inv_to_merge[dic_key]})
    
def export_inventory(filename="export_inventory.csv"):
    export_file = open(dir_path + "/" + filename, "w+")
    export_lines = list_convert_to_string()
    export_file.writelines(export_lines)
    export_file.close() 

def list_convert_to_string():
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
    print("-" * (key_width + value_width))
    for key, value in inventory_items:
        value = str(value)
        print("{} {}" .format(value.rjust(value_width), key.rjust(key_width)))
    print("-" * (key_width + value_width))
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