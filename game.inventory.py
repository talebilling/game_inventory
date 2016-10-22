"""
Game Inventory
by Emese Billing, Oct 2016
"""

def add_to_inventory(inv, added_items): # todo rename item to item_key
    for item in added_items:
        if inv.get(item):
            inv[item] += 1
        else:
            inv.update({item : 1})
    display_inventory(inventory)

def import_inventory(filename="import_inventory.csv"): #put file path in code
    database = open(filename, "r+")
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
    display_inventory(inventory)
    
def display_inventory(inv):
    item_numbers = list(inv.values())
    total_number_of_items = sum(item_numbers) 
    print("\nInventory: ")
    for k, v in inv.items():
        print("{} {}" .format(v, k))
    print("Total number of items:", total_number_of_items, "\n")

def export_inventory(filename="export_inventory.csv"): #export all inventory items to a file
    export_file = open(filename, "w+")
    export_lines = list_convert_to_string()
    export_file.writelines(export_lines)
    export_file.close() 

def list_convert_to_string():
    first_line_to_export = "item_name,count\n"
    export_lines = [first_line_to_export]
    dictionary_keys_list = inventory.keys()   
    for key in dictionary_keys_list:
        export_lines.append(key + "," + str(inventory[key]) + "\n")
    return export_lines

#main
#definitions
inventory = {'rope': 1, 
            'torch': 6, 
            'gold coin': 42, 
            'dagger': 1, 
            'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
filename = "input_file.csv"

display_inventory(inventory)
add_to_inventory(inventory, dragon_loot) 
#calling the import function without argument, for reach default file
import_inventory() 
export_inventory()