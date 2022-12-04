sum = 0

def hasOverlap(b1, e1, b2, e2):
    if int(e1) < int(b2) or int(e2) < int(b1):
        return True
    return False

with open('input.txt') as file:
    for line in file:
        pair = line.strip().split(",")
        r1 = pair[0].split("-")
        r2 = pair[1].split("-")
        if not hasOverlap(r1[0], r1[1], r2[0], r2[1]):
            sum += 1

print(sum)