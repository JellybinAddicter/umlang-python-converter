def python_to_umlang_print(parameter):
    if parameter[6] == '"' or parameter[6] == "'":
        parameter = parameter[7:-2]
        isString = True
    else:
        parameter = parameter[6:-1]
        isString = False
    parameter_lbl = parameter.split('\n')

    for line in range(len(parameter_lbl)):
        if isString:
            for i in range(len(parameter_lbl[line])):
                print('식'+('.'*ord(parameter_lbl[line][i]))+'ㅋ')
        else:
            print('식'+parameter+'!')
        
        if line != len(parameter_lbl)-1:
            print('식'+('.'*10)+'ㅋ')

    # isString = False
    # if parameter[6] == "'" or parameter[6] == '"':
    #     isString = True
    # old_stdout = sys.stdout
    # redirected_output = sys.stdout = StringIO()
    # exec(parameter)
    # sys.stdout = old_stdout
    # output_value = redirected_output.getvalue()[:-1]
    # values = output_value.split('\n')
    # if output_value.count('\n') == len(output_value)//2:
    #     for i in range(len(output_value)//2):
    #         print('식'+('.'*10)+'ㅋ')

    # if len(parameter) == 7:
    #     print('식'+('.'*10)+'ㅋ')
    # for value in values:
    #     if isString:
    #         for i in range(len(value)):
    #             print('식'+('.'*ord(value[i]))+'ㅋ')
    #     else:
    #         try:
    #             int(value)
    #             print('식'+value+'!')
    #         except(ValueError):
    #             for i in range(len(value)):
    #                 print('식'+('.'*ord(value[i]))+'ㅋ')