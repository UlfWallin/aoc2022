inp = ""
with open("input.txt") as file:
    inp = file.readline()

mlen = 4 # change to 14 for part two
chrs = len(inp)
for i in range(1, chrs - mlen - 1):
    b = i
    e = i + mlen
    ch = inp[b:e]

    if len(set(ch)) == mlen:
        print(ch, i + mlen)
        break