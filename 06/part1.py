with open("input.txt") as file:
    inp = file.readline()

mlen = 4 # change to 14 for part two
for i in range(1, len(inp) - mlen - 1):
    ch = inp[i:i+mlen]
    if len(set(ch)) == mlen:
        print(ch, i + mlen)
        break