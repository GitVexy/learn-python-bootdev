def get_quest_status(progress):
    return progress["entity"]["character"]["quests"]["Dragon_Slayer"]["status"]
                   # 1         2            3         4                key

get_quest_status({
    "entity": {                                 # 1 layer
    "character": {                              # 2 layers
    "name": "Kaladin",  
    "quests": {                                 # 3 layers
    "bridge_run": {"status": "In Progress",},
    "Dragon_Slayer": {"status": "Completed",},  # 4 layers + key
            },}}})

{"entity": {"character": {"name": "Kaladin","quests": {"bridge_run": {"status": "In Progress",},"talk_to_syl": {"status": "Completed",},},}}}
