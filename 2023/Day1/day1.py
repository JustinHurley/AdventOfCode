import re

def findFirstNumber(s, rev=False):
    # Find first digit
    earliest = len(s)
    number = None
    i = 0
    while i < earliest:
        if s[i].isdigit():
            earliest = i
            number = int(s[i])
        i += 1

    # Find first word 
    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    if rev:
        numbers = {'eno': 1, 'owt': 2, 'eerht': 3, 'ruof': 4, 'evif': 5, 'xis': 6, 'neves': 7, 'thgie': 8, 'enin': 9}
    for n in numbers.keys():
        pos = s.find(n)
        if pos != -1 and pos < earliest:
                earliest = pos
                number = numbers[n]
    return number


def getFirstAndLast(s):
    return findFirstNumber(s), findFirstNumber(s[::-1], True)


data = open('data.txt', 'r')
lines = data.readlines()
calibration = 0
for line in lines:
    first, last = getFirstAndLast(line)
    calibration += (first*10 + last)
print(calibration)

