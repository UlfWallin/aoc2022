def secIncludes(b1, e1, b2, e2):
    if int(b1) >= int(b2) and int(e1) <= int(e2) or int(b2) >= int(b1) and int(e2) <= int(e1):
        return True
    return False

sum = 0
with open('input.txt') as file:
    for line in file:
        pair = line.strip().split(",")
        r1 = pair[0].split("-")
        r2 = pair[1].split("-")
        if secIncludes(r1[0], r1[1], r2[0], r2[1]):
            sum += 1

print(sum)