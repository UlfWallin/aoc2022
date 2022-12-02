sum = 0
top_three = [0] * 3
with open('input.txt') as file:
    for line in file:
        if line.strip() == '':
            # Sum 
            if sum > min(top_three):
                i = top_three.index(min(top_three))
                top_three[i] = sum
            sum = 0
        else:
            sum += int(line)
if sum > min(top_three):
    i = top_three.index(min(top_three))
    top_three[i] = sum

print(top_three[0] + top_three[1] + top_three[2])
