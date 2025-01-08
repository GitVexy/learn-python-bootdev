def get_odds_and_evens(numbers):
    num_odds = 0
    num_evens = 0

    # Don't touch above this line

    for n in numbers:
        if n % 2 == 1:
            num_odds += 1
        else:
            num_evens += 1
    return num_odds, num_evens
