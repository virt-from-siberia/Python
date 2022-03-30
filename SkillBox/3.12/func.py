def some_func():
    print('Hello world')


some_func()

my_list = [3, 14, 15, 45, 7]


def func_with_param(param, param2):
    print('Func with param', param, param2)


for element in my_list:
    func_with_param(element, element)


def power(nember, pow):
    print('Func with param', nember, pow)
    power_value = nember * pow
    return power_value


for element in my_list:
    result = power(element, 10)
    print('result', result)


def create_default_user():
    name = 'Vasily'
    age = 27
    return name, age


user_name, user_age = create_default_user()

print(user_name, user_age)



























