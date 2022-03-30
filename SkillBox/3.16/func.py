
def multiplay(number_1, number_2):
    print('Function called with prametrs', number_1, number_2)
    if isinstance(number_1, int):
        value = number_1 * number_2
        return value
    return 'error'

print(multiplay(number_1=42, number_2=27))
print(multiplay(number_1='hello', number_2=34))

def elephant_to_free(some_list):
    elephant_found = 'elephant' in some_list
    if elephant_found:
        some_list.remove('elephant')
        print('Elephant is free')

    return elephant_found

zoo = ['lion', 'elephant', 'monekey', 'skuns', 'horse', 'elephant']

elephant_to_free(some_list=zoo)
print(zoo)

elephant_to_free(zoo)
print(zoo)
