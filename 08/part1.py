forest = []
visible = []
with open("input.txt") as file:
    for line in file:
        forest.append(list(map(int,line.strip())))

width = len(forest[0])
visible.append([0] * len(forest[0]))
# Check rows
for i, row in enumerate(forest[:-1]):
    visible.append([0] * len(forest[0]))

    left_tree = 0
    lmax = row[0]
    rmax = row[width - 1]
    for j, tree in enumerate(row[:-1]):
        col = list(map(lambda x: x[j], forest))
        tmax = col[0]
        bmax = col[len(col) - 1]
        if j > 0 and i > 0:
            tmax = max(col[:i])
            bmax = max(col[i+1:])
            lmax = max(row[:j])
            rmax = max(row[j+1:])
        if tree > lmax or tree > rmax or tree > tmax or tree > bmax:
            visible[i][j] = 1

# Check columns
visible[0] = [1] * len(forest[0])
visible[len(visible)-1] = [1] * len(forest[0])
for vr in visible:
    vr[0] = 1 
    vr[len(visible)-1] = 1

sum_visible = sum(sum(t) for t in visible)

print(sum_visible)
