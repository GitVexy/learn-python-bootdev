def combat_evaluation(player_power, enemy_defense):

    advantage, disadvantage, evenly_matched = (
        player_power > enemy_defense,
        player_power < enemy_defense,
        player_power == enemy_defense
    )

    return advantage, disadvantage, evenly_matched
