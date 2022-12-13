from functools import reduce

forest = []
scenic_score = []

def get_view(center: int, height: int, arr, inc: int):
    if center == 0 or center == len(arr) - 1:
        return(0)
    idx = center + inc
    view = 1
    while height > arr[idx]:
        if idx == 0 or idx == len(arr) -1:
            break
        idx += inc
        view += 1

    return(view)

l = get_view(2, 5, [3,3,5,4,9], -1)
u = get_view(3, 5, [3,5,3,5,3], -1)
d = get_view(3, 5, [3,5,3,5,3], 1)
r = get_view(2, 5, [3,3,5,4,9], 1)
print(u,l,d,r)
with open("input.txt") as file:
    for line in file:
        forest.append(list(map(int,line.strip())))

for i, row in enumerate(forest):
    for j, tree in enumerate(row):
        col = list(map(lambda x: x[j], forest))
        w = len(col)-1
        l = get_view(j, tree, row, -1)
        r = get_view(j, tree, row, 1)
        u = get_view(w - i, tree, col, -1)
        d = get_view(w - i, tree, col, 1)
        scenic_score.append(u * l * d * r)

print(max(scenic_score))