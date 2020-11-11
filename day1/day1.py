input_file = open('input.txt', 'r')

input_str = input_file.readline()

current_floor = 0
first_time_basement = 0
current_step = 1

for direction in input_str:
    if direction == '(':
        current_floor += 1
    elif direction == ')':
        current_floor -= 1
    if first_time_basement == 0 and current_floor == -1:
        first_time_basement = current_step
    current_step += 1

print('Part one: {0}, Part two: {1}'.format(current_floor, first_time_basement))
