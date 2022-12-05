import re

#crates = ['TRGWQMFP','RFH','DSHGVRZP','GWFBPHQ','HJMSP','LPRSHTZM','LMNHTP','RQDF','HPLNCSD']
crates = ['NZ', 'DCM', 'P']
instructions = [] # ['move 1 from 2 to 1', 'move 3 from 1 to 3', 'move 2 from 2 to 1', 'move 1 from 1 to 2']

instr_start = False
with open('sample.txt') as file:
    for line in file:
        if line.strip() == '':
            instr_start = True
        
        if instr_start and line.strip() != '':
            instructions.append(line)

#p = re.compile('[A-Z]*')
#print(p.findall('[Z] [M] [P]'))

for instr in instructions:
    parts = instr.split()
    num = int(parts[1])
    cf = int(parts[3])-1
    ct = int(parts[5])-1
    print(num, cf, ct)

    src = crates[cf][:num]
    crates[cf] = crates[cf][num:]
    crates[ct] = src[::-1] + crates[ct]
    print(crates)

    # lines = [line.rstrip() for line in file]
result = ""
for crate in crates:
    result += crate[:1] 
print(result)
