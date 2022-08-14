# function which convert python code to umlang
def python_to_umlang_print(parameter):
    # check if it's string
    if parameter[6] == '"' or parameter[6] == "'":
        # get only print()'s parameter
        parameter = parameter[7:-2]
        isString = True
    else:
        parameter = parameter[6:-1]
        isString = False

    # lbl: line by line 킹아
    parameter_lbl = parameter.split('\n')

    for line in range(len(parameter_lbl)):
        if isString:
            for i in range(len(parameter_lbl[line])):
                print('식'+('.'*ord(parameter_lbl[line][i]))+'ㅋ')
        else:
            print('식'+parameter+'!')
        
        # if it isn't last line, print \n with umlang
        if line != len(parameter_lbl)-1:
            print('식'+('.'*10)+'ㅋ')