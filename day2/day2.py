input_file = open('input.txt', 'r')

total_square_feet = 0
total_ribbon = 0
for current_line in input_file:
    length, width, height = [int(x) for x in current_line.split('x')]
    total_square_feet += 2*length*width + 2*width*height + 2*height*length
    s1, s2 = sorted([length, width, height])[:2]
    total_square_feet += s1*s2
    total_ribbon += 2*s1+2*s2 + length*width*height

print('Part one: {0}, Part two: {1}'.format(total_square_feet, total_ribbon))
