from collections import defaultdict

def count_enemies(enemy_names):
    enemies_dict = defaultdict(int)     # init defaultdict with default value of type int
    
    for enemy_name in enemy_names:      # loop through names
        enemies_dict[enemy_name] += 1   # update key value. if it doesn't exist, it will default to 1
        
    return dict(enemies_dict)           # return as a regular dictionary type