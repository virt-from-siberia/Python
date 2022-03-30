

# open() - открыть файл на файловой системе
ff = open('lesson_004/lecture_snippets/05_builtin.py', 'r', encoding='UTF8')
for line in ff:
    print(line, end='')
ff.close()
# будет целый урок