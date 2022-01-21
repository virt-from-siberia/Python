# еще вариант
file_name = 'pushkin.txt'
file = open(file_name, mode='r', encoding='utf8')
line = True
while line:
    line = file.readline()
    if 'красавица' in line:
        print('Красавица найдена в строке', line)
        break
else:
    print('Тут красавиц нет')
file.close()
