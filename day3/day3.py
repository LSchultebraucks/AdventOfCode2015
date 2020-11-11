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

house_dict = defaultdict(int)
santa_current_x = 0
santa_current_y = 0
robot_current_x = 0
robot_current_y = 0
is_santa_move = True
for direction in input_str:
    if is_santa_move:
        if direction == '^':
            santa_current_y += 1
        elif direction == 'v':
            santa_current_y -= 1
        elif direction == '>':
            santa_current_x += 1
        elif direction == '<':
            santa_current_x -= 1
        current_pos = '{0}:{1}'.format(santa_current_y, santa_current_x)
        house_dict[current_pos] += 1
        is_santa_move = False
    elif not is_santa_move:
        if direction == '^':
            robot_current_y += 1
        elif direction == 'v':
            robot_current_y -= 1
        elif direction == '>':
            robot_current_x += 1
        elif direction == '<':
            robot_current_x -= 1
        current_pos = '{0}:{1}'.format(robot_current_y, robot_current_x)
        house_dict[current_pos] += 1
        is_santa_move = True

visited_houses_santa_robot = len(house_dict.items())

print('Part one: {0}, Part two: {1}'.format(visited_houses, visited_houses_santa_robot))
