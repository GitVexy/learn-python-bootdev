def find_missing_ids(first_ids, second_ids):
    return sorted(list(set(first_ids) - set(second_ids)))

print(find_missing_ids([1,2,3,3], [2]))