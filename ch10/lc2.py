
def merge(dict1, dict2):
    
    output = {}
    
    for item in dict1:
        output[item] = dict1[item]
    for item in dict2:
        output[item] = dict2[item]
    
    return dict(output)


def total_score(score_dict):
    
    output = 0
    
    for score in score_dict:
        output += score_dict[score]
    
    return output


two_towers = {"Frodo": "One Ring", "Aragorn": "Narsil"}
rotk = {"Aragorn": "Andúril", "Gandalf": "Glamdring"}

print(merge(two_towers, rotk))
print(total_score({"Aragorn": 1, "Gandalf": 2}))