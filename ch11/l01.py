def remove_duplicates(spells):
    seen   = set()
    unique = []

    for spell in spells:
        if spell not in seen:
            seen.add(spell)
            unique.append(spell)
    return unique


def alt_remove_duplicates(spells):
    return sorted(list(set(spells)))



test = ["Jargon", "Molbruk", "Jargon", "Fire Blast"]
print(remove_duplicates(test))
print(alt_remove_duplicates(test))