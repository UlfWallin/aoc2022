win = {'C': 'A', 'B': 'C', 'A': 'B'}
lose = {'A': 'C', 'C': 'B', 'B': 'A'}
sum = 0
with open('input.txt') as file:
    for line in file:
        opponent = line[0]
        action = line[2]
        if action == 'Y':
            me = opponent
        elif action == 'X':
            me = lose[opponent]
        else:
            me = win[opponent]

        sum += ord(me) - ord('A') + 1

        match (me, opponent):
            case ('A', 'C'):
                sum += 6
            case ('C', 'B'):
                sum += 6
            case ('B', 'A'):
                sum += 6
                   
        if me == opponent:
            sum += 3

print(sum)