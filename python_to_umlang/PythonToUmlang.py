print('input all python code and enter {end} to finish')

python_code = ''

while True:
    a = input()
    if a != '{end}':
        python_code += a+'\n'
    else:
        break

python_code = python_code[:-1]

print(python_code)