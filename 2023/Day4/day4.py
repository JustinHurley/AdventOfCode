from collections import deque
data = open('test.txt', 'r')
lines = data.readlines()

class Scratchcard:
    def __init__(self, row, win_set=set(), curr_set=set()):
        self.row = row
        self.win_set = set(win_set)
        self.curr_set = set(curr_set)
    
    def get_score(self):
        intersection = self.win_set.intersection(self.curr_set)
        if len(intersection) == 1:
            return 1
        elif len(intersection) > 1:
            return 2**(len(intersection)-1)
        else:
            return 0
    
    def get_num_matches(self):
        return len(self.curr_set.intersection(self.win_set))


def line_to_scratchcard(s):
    split = s.split('|')
    winners = split[0].split(' ')
    current = split[1].split(' ')
    win_set, curr_set = set(), set()
    for x in winners[2:]:
        if x != '':
            win_set.add(x)
    for y in current:
        if y != '':
            if y[-1] == '\n':
                curr_set.add(y[:-1])
            else: 
                curr_set.add(y)
    row = 1
    if winners[1] == '' and winners[2] == '':
        row = winners[3].replace(':', '')
    elif winners[1] == '':
        row = winners[2].replace(':', '')
    else:
        row = winners[1].replace(':', '')

    return Scratchcard(int(row), win_set, curr_set)


def part1():
    ans = 0
    for line in lines:
        scratchcard = line_to_scratchcard(line)
        print(scratchcard.row, scratchcard.get_score(), scratchcard.win_set, scratchcard.curr_set)
        ans += scratchcard.get_score()
    print(ans)

def part2():
    ans = 0
    cards = {}
    for line in lines:
        scratchcard = line_to_scratchcard(line)
        cards[scratchcard.row] = scratchcard
    
    Q = deque(cards.keys())
    while Q:
        # Pop line
        curr = cards[Q.pop()]
        ans += 1
        num_matches = curr.get_num_matches()
        for i in range(curr.row+1, curr.row+num_matches+1):
            Q.appendleft(i)
    print(ans)
        

def run():
    part2()

run()