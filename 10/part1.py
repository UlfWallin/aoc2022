from collections import deque

sig_s = []
instructions = deque([])
with open('input.txt') as file:
    for line in file:
        instructions.append(line.strip())

cycle = 1
x_reg = 1
call_stack = deque([])
instr = instructions.popleft()
c_len = 2 if instr.startswith('addx') else 1
call_stack.append({'instruction': instr, 'cycle': c_len})

while len(call_stack) > 0:
    call_stack[0]['cycle'] -= 1
    if call_stack[0]['cycle'] == 0:
        # execute
        exec = call_stack.popleft()
        if exec['instruction'] == 'noop':
            pass
        else:
            parts = exec['instruction'].split()
            x_reg += int(parts[1])

        if len(instructions) > 0:        
            instr = instructions.popleft()
            call_stack.append({'instruction': instr, 'cycle': 2 if instr.startswith('addx') else 1})
    cycle += 1
    if cycle % 20 == 0 and cycle < 20:
        sig_s.append(cycle * x_reg)
        print(cycle, cycle * x_reg)
    
    if (cycle + 20) % 40 == 0:
        sig_s.append(cycle * x_reg)
        print(cycle, cycle * x_reg)

print(sum(sig_s))