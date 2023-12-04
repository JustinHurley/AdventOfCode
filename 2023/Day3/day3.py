data = open('input.txt', 'r')
lines = data.readlines()

def issymbol(c):
    return c != '.' and not c.isdigit() and c != '\n'

# checks [l, r] inclusive
def check(line, l, r, row):
    for i in range(l-1, r+1):
        # If col in bounds
        if i >= 0 and i < len(line):
            if row > 0:
                if issymbol(lines[row-1][i]):
                    return True
            if row < len(lines)-1:
                if issymbol(lines[row+1][i]):
                    return True
    if l > 0 and issymbol(line[l-1]):
        return True
    if r < len(line)-1 and issymbol(line[r]):
        return True
    return False
            



def part1():
    ans = 0
    for row, line in enumerate(lines):
        print(f"ROW: {row}")
        fast, slow = 0, 0
        while fast < len(line):
            while fast < len(line) and line[fast].isdigit():
                fast += 1
            if slow != fast and check(line, slow, fast, row):
                ans += int(line[slow:fast])
                print(line[slow:fast])
            fast += 1
            slow = fast
    print(ans)

def in_bounds(r, c):
    return r >= 0 and r <= len(lines) and c >= 0 and c <= len(lines[0])

def find_num(row, col):
    l, r = col, col
    while l > 0 and lines[row][l-1].isdigit():
        l -= 1
    while r < len(lines[0])-1 and lines[row][r+1].isdigit():
        r += 1
    return int(lines[row][l:r+1])
        

def find_ratio(row, col):
    nums = []
    for c in range(col-1, col+2):
        if in_bounds(row-1, c) and lines[row-1][c].isdigit():
            nums.append(find_num(row-1, c))
            break
    for c in range(col-1, col+2):
        if in_bounds(row-1, c) and lines[row+1][c].isdigit():
            nums.append(find_num(row+1, c))
            break
    if in_bounds(row, col-1) and lines[row][col-1].isdigit():
        nums.append(find_num(row, col-1))
    if in_bounds(row, col+1) and lines[row][col+1].isdigit():
        nums.append(find_num(row, col+1))
    
    if len(nums) == 2:
        return nums[0]*nums[1]
    return 0
        


# dfs from every gear
def part2():
    rows = len(lines)
    ans = 0
    for row in range(rows):
        for col in range(len(lines[row])):
            if lines[row][col] == '*':
                print(f'Found gear at: {row}, {col}')
                ans += find_ratio(row, col)
    print(ans)
