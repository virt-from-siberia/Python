# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as ex:
#         print(f'an error occurred: {ex}')
#
#
# print(divide(4, 2))
# print(divide(4, 0))

# file = None
# try:
#     file = open(r'C:\tmp\lol.txt')
#     data = file.read()
# except FileExistsError as ex:
#     print(f'error has occurred. Description: {ex}')
# else:
#     print('ELSE')
# finally:
#     if file:
#         file.close()

def get_int() -> int:
    while True:
        try:
            replay = int(input('Enter the number'))
            return replay
        except:
            print('You should enter only numbers, try again')
            continue


result = get_int()
print(result)
