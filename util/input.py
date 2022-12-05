def read_to_nl(filename):
    contents = ''
    with open(filename) as file:
        for line in file:
            if line.strip() == '':
                break
            else:
                contents += line
    return(contents)