from print_converter import isPrint, printParameter, python_to_umlang_print
import sys
from io import StringIO

from variable_converter import isVariable, python_to_umlang_variable

print('input all python code and enter {end} to finish')

python_code = ''''''

# input codes
while True:
    a = input()
    if a != '{end}':
        python_code += a+'''\n'''
    else:
        break

# to erase \n in end of variable
python_code = python_code[:-1]

# check whether the code is valid
try:
    # make exec() to not print
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    # execute to check
    exec(python_code)
    sys.stdout = old_stdout
    _ = redirected_output.getvalue()
except:
    # if some error occured, it means there is problem
    print('This python code is invalid.')
    quit()

print('어떻게')

python_code_splited = python_code.split('\n')
line_count = len(python_code_splited)
isPrinted = False
variable_id = 0
variable_stored = {}
for i in range(line_count):
    # print code
    # check if there is print
    if isPrint(python_code_splited[i]):
        # to prevent case like print("print()"), check if it is in print()    
        if isPrinted:
            print('식ㅋ')

        S = printParameter(i, line_count, python_code_splited)
        python_to_umlang_print(S)
        isPrinted = True

    elif isVariable(python_code_splited[i]):
        print('엄', end='')
        print('어'*variable_id,end='')
        python_to_umlang_variable(python_code_splited[i], variable_stored, variable_id)
        variable_id += 1

print('이 사람이름이냐ㅋㅋ')