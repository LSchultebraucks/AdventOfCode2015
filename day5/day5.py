input_file = open('input.txt', 'r')

lines = input_file.readlines()

nice_string_count = 0
vowels = ['a', 'e', 'i', 'o', 'u']
black_list = ['ab', 'cd', 'pq', 'xy']

for string in lines:
    has_black_list_strings = False
    vowels_count = len([x for x in string if x in vowels])
    previous_char = ''
    has_twice_in_a_row_character = False
    for char in string:
        if char == previous_char:
            has_twice_in_a_row_character = True
        previous_char = char
    for black_list_word in black_list:
        if string.find(black_list_word) != -1:
            has_black_list_strings = True
    if vowels_count >= 3 and has_twice_in_a_row_character and not has_black_list_strings:
        nice_string_count += 1


new_rules_nice_string_count = 0
for string in lines:
    letter_repeat_between = not any([string[i] == string[i+2] for i in range(len(string)-2)])
    has_twice_pairs = any([(string.count(string[i:i+2])>=2) for i in range(len(string)-2)])
    if not letter_repeat_between and has_twice_pairs:
        new_rules_nice_string_count += 1

print('Part one: {0}, Part two: {1}'.format(nice_string_count, new_rules_nice_string_count))
