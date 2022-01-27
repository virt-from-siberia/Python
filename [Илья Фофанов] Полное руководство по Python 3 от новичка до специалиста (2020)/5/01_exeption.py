def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        print(f'an error occurred: {ex}')


print(divide(4, 2))
print(divide(4, 0))
