def get_most_common_enemy(enemies_dict):
    if not enemies_dict:
        return None
    
    max_so_far  = float("-inf")
    max_name    = ""
    
    for enemy in enemies_dict:
        if enemies_dict[enemy] > max_so_far:
            max_so_far = enemies_dict[enemy]
            max_name = enemy
            
    return max_name


print(get_most_common_enemy({
    "jackal": 1,
    "kobold": 2,
    "soldier": 3,
    "gremlin": 5
    }))