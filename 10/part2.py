from collections import deque

instructions = deque([])
with open('input.txt') as file:
    for line in file:
        instructions.append(line.strip())

cycle = 1
x_reg = 1
call_stack = deque([])
instr = instructions.popleft()
call_stack.append({'instruction': instr, 'cycle': 2 if instr.startswith('addx') else 1})

curr_row = ''

while len(call_stack) > 0:
    sprite_pos = x_reg + 1
    row_pos = cycle % 40
    if row_pos >= sprite_pos - 1 and row_pos <= sprite_pos + 1:
        curr_row += '#'
    else:
        curr_row += '.'

    call_stack[0]['cycle'] -= 1
    if call_stack[0]['cycle'] == 0:
        exec = call_stack.popleft()
        if exec['instruction'] == 'noop':
            pass
        else:
            parts = exec['instruction'].split()
            x_reg += int(parts[1])

        if len(instructions) > 0:        
            instr = instructions.popleft()
            call_stack.append({'instruction': instr, 'cycle': 2 if instr.startswith('addx') else 1})
    if cycle % 40 == 0:
        print(curr_row)
        curr_row = ''
        
    cycle += 1