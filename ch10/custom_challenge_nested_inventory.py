from collections import defaultdict

def calculate_inventory(
    resources   # dict with party member names as keys and item dictionary as value
    ):
    
    if not resources:
        return {}
    
    inventory_summary = defaultdict(int) # dict for tracking total supplies across party-members:
    
    for member in resources: # For "Sally", "Jack", "Luna"
        for item in resources[member]: # For "potion", "apple"
            
            # Outputs typeError warning, and skips item
            if type(item) != str:
                print(f"Warning: Skipping item {item}. Expected a string, got ({type(item)})")
                continue
            
            # Outputs quantity warning, and skips item
            if resources[member][item] > 1000:
                print(f"Warning: Skipping item {item}. Quantity  is suspiciously high ({resources[member][item]}).")
                continue

            # Outputs negative quantity warning, and skips item
            if resources[member][item] < 0:
                print(f"Warning: Skipping item {item}. Quantity is negative ({resources[member][item]}).")
                continue
            
            # Outputs case sensitivity warning, but keeps item
            if item.lower() in inventory_summary and item != item.lower():
                print(f"Warning: Item name '{item}' merged with key '{item.lower()}'. Correct capitalization?")
                
            inventory_summary[item.lower()] += resources[member][item]  # Summary at key "item" += x where "item" : x
    
    return dict(inventory_summary)

# Should handle empty nested dict
print("\nInventory:\n",
    calculate_inventory({
    "Sally" : {"potion": 2, "apple": 3},
    "Jack"  : {"Potion": 1, "sword": 1},
    "Luna"  : {"shield": 1, "APPLE": 5},
    "Boots" : {}}),
    "\n")

# Should handle empty dict
print("\nInventory:\n",
    calculate_inventory({}),
    "\n")

# Should handle negative numbers, large numbers, and odd case
print("\nInventory:\n",
    calculate_inventory({
    "Sally" : {"potion": 2, "apple": 3},
    "Jack"  : {"Potion": 1, "sword":-1},
    "Luna"  : {"shield": 1, "APPLE": 5},
    "Boots" : {"potion":-5, "apple": 5000}}),
    "\n")

# Should raise exception and abort
print("\nInventory:\n",
    calculate_inventory({"Rascal": {123: 2, "potion": -3}}),
    "\n")