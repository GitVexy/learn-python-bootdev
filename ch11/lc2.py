def count_vowels(text):
    vowels = set("AEIOUaeiou")
    count = 0
    unique = set()
    
    for char in text:
        if char in vowels:
            count += 1
            unique.add(char)
    
    return count, unique





from collections import defaultdict
def alt_count_vowels(text, text2):
    vowels = set("AEIOUaeiou")
    count = 0
    unique = set()
    vowel_counts = defaultdict(int)
    all_text = text + text2
    
    for char in all_text:
        if char in vowels:
            count += 1
            unique.add(char)
            vowel_counts[char] += 1
    
    max_so_far = float("-inf")
    max_vowel = ''
    for vowel in vowel_counts:
        if vowel_counts[vowel] > max_so_far:
            max_so_far = vowel_counts[vowel]
            max_vowel = vowel
        elif vowel_counts[vowel] == max_so_far:
            max_so_far = vowel_counts[vowel]
            max_vowel = f"{vowel} and {max_vowel}"
        
    
    return f"Vowels: {count}\nUnique vowels: {unique}\nMost common vowel: {max_vowel}, which {"both " if len(max_vowel) > 1 else ""}appeared {max_so_far} times\n"

print(alt_count_vowels("Heello", "world"))
print(alt_count_vowels("Did someone say Thunderfury, Blessed Blade of the Windseeker?", "NOBODY DID! WHY AM I SHOUTING!?"))
#{"a", "e", "i", "o", "u"}