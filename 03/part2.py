prio = 0
group = []
shared = []
with open('input.txt') as file:
    for i, line in enumerate(file):
        group.append(line.strip())
        if (i + 1) % 3 == 0:
            shared.append(set(group[0]) & set(group[1]) & set(group[2]))
            group = []
    for x in shared:
        item = list(x)[0]
        if item >= 'a':
            prio += ord(item) - ord('a') + 1
        else:
            prio += ord(item) - ord('A') + 27
print(prio)