def python_to_umlang_print(parameter):
    if len(parameter) == 8:
        if parameter[6] == '"' or parameter[6] == "'":
            print('invalid print expression')
            return
    if (parameter[6] == parameter[-2]) and (parameter[6] == "'" or parameter[6] == '"'):
        for i in range(7, len(parameter)-2):
            print('식'+('.'*ord(parameter[i]))+'ㅋ')
    elif (parameter[6] != '"' and parameter[6] != "'") and (parameter[-2] != '"' and parameter[-2] != "'"):
        print('식'+parameter[6:-1]+'!')
    else:
        print('invalid print expression')


python_to_umlang_print(input())