prio = 0
with open('input.txt') as file:
    for line in file:
        sz = int(len(line) / 2)
        first = line[:sz]
        second = line[sz:]
        shared = set(first) & set(second)
        
        for item in shared:
            if item >= 'a':
                prio += ord(item) - ord('a') + 1
            else:
                prio += ord(item) - ord('A') + 27
print(prio)