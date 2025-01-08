

def track_power_level(
    party_members # list of tuples (name, level)
    ):
    if party_members == []:
        return (f"Highest power: Nobody, with 0 power\nAverage power: 0.0\nTotal power: 0\n\nEmpty party list")
        
    highest_name    = ""
    highest         = 0
    power_sum       = 0
    party_count     = 0
    
    for member in party_members:
        party_count     += 1
        power_sum       += member[1]
        
        if member[1] > highest:
            highest      = member[1]
            highest_name = member[0]
            
        elif member[1]  == highest:
            highest_name = sorted([highest_name, member[0]])[0]

    
    average_power = round(power_sum / party_count, 2)
    
    return f"Highest power: {highest_name}, with {highest} power\nAverage power: {average_power}\nTotal power: {power_sum}"

print(f"Sort case: \n{track_power_level([("Sally", 120), ("Jack", 85), ("Luna", 150), ("Ava", 150)])}\n")
print(f"Zero case: \n{track_power_level([("Harry", 777), ("Erik", 71), ("Paul", 0  ), ("Tim", 90 )])}\n")
print(f"Neg. case: \n{track_power_level([("Marie", 610), ("Mick", 99), ("Jane", -10), ("Sam", 50 )])}\n")
print(f"Empty case:\n{track_power_level([])}")


""" Challenge: Power Level Tracker

Your adventuring party consists of members with varying "power levels" (an integer value), representing their combat capability.

Write a function called track_power_levels that:

    Accepts:
        A list of party members represented as tuples, where each tuple contains the member's name (string) and their power level (integer). Example: [("Sally", 120), ("Jack", 85)].

    Calculates:
        The highest power level and its owner.
        The average power level of the party, rounded to 2 decimal places.
        The total sum of power levels.

    Returns:
        A string formatted as follows:

    "Highest power: NAME (LEVEL)\nAverage power: AVERAGE\nTotal power: SUM"

Example Input:

party = [("Sally", 120), ("Jack", 85), ("Luna", 150), ("Rex", 90)]

Expected Output:

"Highest power: Luna (150)\nAverage power: 111.25\nTotal power: 445"

You’ll need to consider:

    Iterating over a list of tuples to perform calculations.
    Keeping track of the "highest power level" while iterating.
    Using the length of the party to calculate averages. """