code = []

while True:
    inp = input()
    if inp == '어떻게':
        continue
    if inp == '':
        continue
    if inp == '이 사람이름이냐ㅋㅋ':
        break

    code.append(inp)

print(code)