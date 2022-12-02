m = {'X': 'A', 'Y': 'B', 'Z': 'C'}
sum = 0
with open('input.txt') as file:
    for line in file:
        opponent = line[0]
        me = m[line[2]]
        print(opponent, me)
        sum += ord(me) - ord('A') + 1

        match (me, opponent):
            case ('A', 'C'):
                sum += 6
                print('win')
            case ('C', 'B'):
                sum += 6
                print('win')
            case ('B', 'A'):
                sum += 6
                print('win')
                   
        if me == opponent:
            print('draw')
            sum += 3

print(sum)