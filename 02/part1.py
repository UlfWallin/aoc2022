m = {'X': 'A', 'Y': 'B', 'Z': 'C'}
sum = 0
with open('input.txt') as file:
    for line in file:
        opponent = line[0]
        me = m[line[2]]
        sum += ord(me) - ord('A') + 1

        match (me, opponent):
            case ('A', 'C') | ('C', 'B') | ('B', 'A'): 
                sum += 6
            case _:   
                if me == opponent:
                    sum += 3

print(sum)