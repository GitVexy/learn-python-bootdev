def update_inventory(
    inventory,  # dictionary
    sold_items  # list
    ):
    for item in sold_items:
        if item in inventory:
            if inventory[item] == 0:
                print(f"{item} out of stock!")
            else:
                inventory[item] -= 1
        else:
            print(f"{item} not available.")
    
    return inventory

inventory = {"potion": 5, "sword": 2, "shield": 3}
sold_items = ["potion", "sword", "sword", "potion", "cloak"]
print(update_inventory(inventory, sold_items))



""" Challenge: Inventory Management

You're running a shop for adventurers, and you need to keep track of your inventory. Customers buy items, and the shop's stock must update accordingly. Write a function, update_inventory, that:

    Takes in two arguments:
        A dictionary (inventory) where keys are item names (strings) and values are the stock count (integers).
        A list of item names (sold_items) representing items that customers have purchased.

    For each item in sold_items, decrease its stock count in the inventory by 1.

    If an item in sold_items doesn’t exist in the inventory (they bought something you don’t stock!), ignore it.

    Return the updated inventory.

Example Input:

inventory = {"potion": 5, "sword": 2, "shield": 3}
sold_items = ["potion", "sword", "sword", "potion", "cloak"]

Expected Output:

{"potion": 3, "sword": 0, "shield": 3}

Notice:

    "potion" was sold twice, so its count decreases by 2.
    "sword" was bought twice, and now its stock is 0.
    "cloak" isn't in the inventory, so nothing happens for it.
    "shield" remains untouched because it wasn't sold.

Try crafting the function! I encourage you to iterate through the list of sold_items and use a dict lookup with square brackets. Let me know where you might get snagged! """