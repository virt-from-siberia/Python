import os
import time

path = 'C:/Windows/help'
path_normalized = os.path.normpath(path)
print(path_normalized)

# Пройтись по всем файлам в директории.
count = 0
for dirpath, dirnames, filenames in os.walk(path_normalized):
    print('*' * 27)
    print(dirpath, dirnames, filenames)
    print(os.path.dirname(dirpath))
    count += len(filenames)
    for file in filenames:
        full_file_path = os.path.join(dirpath, file)
        secs = os.path.getctime(full_file_path)
        file_time = time.gmtime()
        print(full_file_path, secs, file_time)

print(count)

print(__file__, os.path.dirname(__file__))
