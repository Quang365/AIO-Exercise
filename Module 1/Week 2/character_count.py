def count_character(string):
    character_count = {}

    for character in string:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count

print(count_character("Happiness"))