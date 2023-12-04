import re

input = open('input.txt', 'r')
lines = input.readlines()

def parse_line(line):
    tokens = re.split(r'[;:]', line)
    game_id = tokens[0][5:]
    r, g, b = 0, 0, 0
    for i in range(1, len(tokens)):
        curr_cubes = tokens[i][1:].replace('\n', '').split(' ')
        for j in range(0, len(curr_cubes)-1, 2):
            curr_num = int(curr_cubes[j])
            curr_color = curr_cubes[j+1].replace(',', '')
            print(curr_num, curr_color)
            if curr_color == 'red':
                r = max(r, curr_num)
            elif curr_color == 'green':
                g = max(g, curr_num)
            elif curr_color == 'blue':
                b = max(b, curr_num)
            else:
                print('Invalid color')
    return r*g*b

ans = 0
for line in lines:
    ans += parse_line(line)
print(ans)
