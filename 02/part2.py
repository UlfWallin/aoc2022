win = {'C': 'A', 'B': 'C', 'A': 'B'}
lose = {'A': 'C', 'C': 'B', 'B': 'A'}
sum = 0
with open('input.txt') as file:
    for line in file:
        opponent = line[0]
        action = line[2]
        if action == 'Y':
            me = opponent
            sum += 3
        elif action == 'X':
            me = lose[opponent]
        else:
            me = win[opponent]
            sum += 6

        sum += ord(me) - ord('A') + 1

print(sum)