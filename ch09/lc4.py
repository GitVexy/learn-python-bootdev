def validate_path(expected_path, character_path):
    count = 0
    name = character_path[0]
    for i in range(len(expected_path)):
        if expected_path[i] == character_path[i+1]:
            count += 1
    percent = (count / len(expected_path)) * 100

    return name, percent

""" 
    Getting the name with character_path[0] instead of pop(0) - perfect!
    Using character_path[i+1] to offset the index since the waypoints start at index 1 - very clever!
    Calculating the percentage correctly using count/len(expected_path) * 100
    Returning both the name and percentage as required

Have you tested this with some of the example cases? For instance, what would your code return for:

expected_path = ["A", "B", "C"]
character_path = ["Hero", "A", "X", "C"]
 """

expected_path = ["A", "B", "C"]
character_path = ["Hero", "A", "X", "C"]
print(validate_path(expected_path, character_path))

# >> ('Hero', 66.66666666666666)

""" That's exactly right! Your code is now working as intended. Let's break down why this output is correct:

    "Hero" - correctly extracted from character_path[0]
    66.66666666666666 - because:
        The character matched 2 out of 3 waypoints (A and C)
        2/3 * 100 = 66.66666666666666

Your solution successfully:

    Extracts the character name
    Compares waypoints with the correct offset
    Calculates the accuracy percentage
    Returns both values in the required format
 """