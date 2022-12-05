import math

def get_instructions(filename):
    instructions = []
    instr_start = False
    with open(filename) as file:
        for line in file:
            if line.strip() == '':
                instr_start = True
            
            if instr_start and line.strip() != '':
                instructions.append(line.strip())
    return(instructions)

def get_crates(filename):
    crates = []
    with open(filename) as file:
        for i, line in enumerate(file):
            #cols = 0
            if line.strip() == '' or line.find('[') < 0:
                break
            if i == 0:
                cols = math.ceil(len(line) / 4)
                crates = [''] * cols

            for col in range(cols):
                crates[col] += line[col * 4 + 1: col * 4 + 2]

    return(list(map(str.strip, crates)))