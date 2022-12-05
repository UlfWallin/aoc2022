import common

filename = 'input.txt'
crates = common.get_crates(filename)
instructions = common.get_instructions(filename) 

for instr in instructions:
    parts = instr.split()
    num = int(parts[1])
    cf = int(parts[3])-1
    ct = int(parts[5])-1

    src = crates[cf][:num]
    crates[cf] = crates[cf][num:]
    crates[ct] = src + crates[ct]
    
result = ""
for crate in crates:
    result += crate[:1] 
print(result)
