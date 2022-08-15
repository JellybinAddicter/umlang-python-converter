def isVariable(line):
    line_splited = line.split('=')
    if len(line_splited) == 2:
        if line_splited[1][0] == '"' or line_splited[1][0] == "'":
            print("Umlang doesn't support string in variable")
            return False
        return True
    else:
        return False

def python_to_umlang_variable(line, variable, variable_id):
    line_splited = line.split('=')
    variable_value = line_splited[-1]
    # if variable_value[0] == '"' or variable_value[0] == "'":
    #     variable[line_splited[0]] = [variable_id, line_splited[-1]]
    #     variable_value_inner = variable_value[1:-1]
    #     for i in range(len(variable_value_inner)):
    #         print('.'*ord(variable_value_inner[i])+'ㅋ')

    #         if i != len(variable_value_inner)-1:
    #             print('엄', end='')
    # else:
    try:
        now = [variable_id, int(line_splited[-1])]
        variable[line_splited[0]] = now
    except(ValueError):
        now = [variable_id, variable[variable_value][1]]
        variable[line_splited[0]] = now
    print('.'*int(now[1]))