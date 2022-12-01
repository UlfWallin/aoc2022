sum = 0
maxSum = 0
with open('input.txt') as file:
    for line in file:
        if line.strip() == '':
            # Sum 
            if sum > maxSum:
                maxSum = sum
            sum = 0
        else:
            sum += int(line)
if sum > maxSum:
    maxSum = sum
print(maxSum)