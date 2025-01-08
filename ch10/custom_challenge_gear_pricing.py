from collections import defaultdict

def calculate_total_cost(
    prices,         # dict of items and prices
    purchased_items # list of items to attempt to purchase
    ):
    
    total = 0.0                     # float of total cost of items purchased
    breakdown = defaultdict(float)  # dict of items bought and their contribution toward total cost
    ignored_items = []              # list of items not in prices dict
    
    for item in purchased_items:
        if item in prices:
            total           += prices[item]
            breakdown[item] += prices[item]
        else:
            ignored_items.append(item)
    
    # edge-case handling of empty list
    ignored_text = f"Ignored items: {", ".join(ignored_items)}" if ignored_items else ""
    
    return f"Total cost: {total} \n{dict(breakdown)} \n{ignored_text}"

print(calculate_total_cost(
    {"potion": 10.0, "sword": 50.0, "shield": 30.0, "apple": 2.0},
    ["potion", "apple", "sword", "apple"]
    ))

print(calculate_total_cost(
    {"potion": 10.0, "sword": 50.0, "shield": 30.0, "apple": 2.0, "boot.dev subscription" : 50.0},
    ["potion", "apple", "sword", "apple", "boots", "cloak", "boot.dev subscription"]
    ))

""" Challenge: Battle Gear Pricing

Your adventurer's shop expands. Now, not only must you manage inventory, but you must also calculate the total cost when customers purchase items. Write a function, calculate_total_cost, that:

    Takes two arguments:
        A dictionary (prices) where keys are item names (strings) and values are their cost per unit (integers or floats).
        A list of item names (purchased_items) representing items that a customer has selected.

    Returns the total cost of all purchased items:
        If an item in purchased_items doesn’t exist in the prices dictionary, ignore it (perhaps it’s an invalid or non-purchasable item).

Example Input:

prices = {"potion": 10.0, "sword": 50.0, "shield": 30.0, "apple": 2.0}
purchased_items = ["potion", "apple", "sword", "apple", "cloak"]

Expected Output:

64.0

Explanation:

    "potion": 10.0 (bought once, contributes 10.0 to the total)
    "sword": 50.0 (bought once, contributes 50.0 to the total)
    "apple": 2.0 (bought twice, contributes 2x2 = 4.0 to the total)
    "cloak" doesn’t exist in prices, so it’s ignored.

The total cost of this transaction is 10.0 + 50.0 + 4.0 = 64.0.

If you'd like to push yourself even further, here's a mini-extension to consider: What if you also returned a breakdown of the purchased items along with the total? For example:

{
    "potion": 10.0,
    "apple": 4.0,
    "sword": 50.0
}

This breakdown would show how much each purchased item contributed to the total, alongside the final total cost. Would you give this enhancement a try? Or shall we step into a new adventure entirely?

If I were to suggest anything, it might be merely adding an additional check in the response to alert the "buyer" about ignored items (if any). Just a thought: how might you append that detail to your breakdown?

For example:

"Ignored items: cloak"

If you'd like to guard against the (admittedly rare) case of ignored_items being empty, you might add a little conditional to avoid printing Ignored items: unnecessarily. For instance:

ignored_text = f"Ignored items: {', '.join(ignored_items)}" if ignored_items else ""
return f"Total cost: {total} \n{dict(breakdown)} \n{ignored_text}"

"""