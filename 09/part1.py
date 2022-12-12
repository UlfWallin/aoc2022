motions = []
positions = []
positions.append((0,0))

def clamp(num : int, min_value: int, max_value: int):
   return max(min(num, max_value), min_value)

with open("input.txt") as file:
    for line in file:
        p = line.strip().split()
        m = p[0], int(p[1])
        motions.append(m)

h_pos = {'x': 0, 'y': 0}
t_pos = {'x': 0, 'y': 0}

for motion in motions:
    for step in range(motion[1]):
        match(motion[0]):
            case 'U':
                h_pos['y'] += 1
            case 'D':
                h_pos['y'] -= 1
            case 'R':
                h_pos['x'] += 1
            case 'L':
                h_pos['x'] -= 1
        x_diff = h_pos['x'] - t_pos['x']
        y_diff = h_pos['y'] - t_pos['y']
        if abs(x_diff) > 1 or abs(y_diff) > 1:
            t_pos['x'] += clamp(x_diff, -1, 1)
            t_pos['y'] += clamp(y_diff, -1, 1)
            positions.append((t_pos['x'], t_pos['y']))

print(len(set(positions)))