from collections import defaultdict

input_file = open('input.txt', 'r')

input_str = input_file.readline()

house_dict = defaultdict(int)
current_y = 0
current_x = 0
for direction in input_str:
    if direction == '^':
        current_y += 1
    elif direction == 'v':
        current_y -= 1
    elif direction == '>':
        current_x += 1
    elif direction == '<':
        current_x -= 1
    current_pos = '{0}:{1}'.format(current_y, current_x)
    house_dict[current_pos] += 1

visited_houses = len(house_dict.items())

print('Part one: {0}, Part two: {1}'.format(visited_houses, None))
