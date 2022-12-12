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

rope = []
for o in range(10):
    rope.append({'x': 0, 'y':0})

for motion in motions:
    for step in range(motion[1]):
        match(motion[0]):
            case 'U':
                rope[0]['y'] += 1
            case 'D':
                rope[0]['y'] -= 1
            case 'R':
                rope[0]['x'] += 1
            case 'L':
                rope[0]['x'] -= 1
        
        for i, knot in enumerate(rope[1:], 1):
            x_diff = rope[i-1]['x'] - knot['x']
            y_diff = rope[i-1]['y'] - knot['y']

            if abs(x_diff) > 1 or abs(y_diff) > 1:
                rope[i]['x'] += clamp(x_diff, -1, 1)
                rope[i]['y'] += clamp(y_diff, -1, 1)
                if i == len(rope) - 1:
                    positions.append((rope[i]['x'], rope[i]['y']))
    print(motion)
    

print(len(set(positions)))