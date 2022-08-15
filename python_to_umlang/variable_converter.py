def isVariable(line):
    line_splited = line.split('=')
    if len(line_splited) == 2:
        return True
    else:
        return False