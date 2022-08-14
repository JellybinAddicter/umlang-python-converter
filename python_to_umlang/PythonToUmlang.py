from print_converter import python_to_umlang_print
import sys
from io import StringIO

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



python_code_splited = python_code.split('\n')
line = len(python_code_splited)
isInPrint = False
isPrinted = False

# print code
for i in range(line):
    # check if there is print
    if 'print(' in python_code_splited[i]:
        # to prevent case like print("print()"), check if it is in print()
        if not isInPrint:
            isInPrint = True
            
            if isPrinted:
                print('식'+('.'*10)+'ㅋ')

            # when print() ends in one line
            if ')' in python_code_splited[i]:
                python_to_umlang_print(python_code_splited[i])
                isInPrint = False
                isPrinted = True
            else:
                # S is a variable which store things in print()
                S = python_code_splited[i]
                # stack to check where print()'s closing bracket ends
                stack = [1]
                for j in range(i+1, line):
                    S += python_code_splited[j]
                    if '(' in python_code_splited[j]:
                        stack.append(0)
                    
                    if ')' in python_code_splited[j]:
                        stack.pop()
                    
                    if len(stack) == 0:
                        python_to_umlang_print(S)
                        isInPrint = False
                        isPrinted = True