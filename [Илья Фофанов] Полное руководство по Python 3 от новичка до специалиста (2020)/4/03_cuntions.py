def greeting():
    '''
    DOCSTRING : Information about the function
    INPUT: no input...
    OUTPUT: Hello
    '''
    print('Hello')


greeting()
help(greeting)


def print_name(name: str = 'Default') -> None:
    print(name)


print_name()


def get_greeting(name: str) -> str:
    return 'Hello' + name


greeting = get_greeting('Ellis')
print(greeting)


def get_sum(a: int, b: int) -> int:
    return a + b


def is_adult(age: int) -> bool:
    return age >= 18


print(type(is_adult))
is_adult = is_adult(20)
print(type(is_adult))
print(is_adult)


def is_palindrome(text: str) -> bool:
    return text == text[::-1]


print(is_palindrome('ароза упала на алапу азора'))


def calc_taxes(p1: int, p2: int, p3: int) -> float:
    return sum((p1, p2, p3)) * 0.06


res = calc_taxes(10, 20, 30)
print(res)


def calc_taxes(*args):
    for x in args:
        print(f"Got payment = {x}")
    return sum(args) * 0.06


calc_taxes(10, 20, 30)


def save_players(**kwargs):
    for k, v in kwargs.items():
        print_name(f"player {k} has rating {v}")


save_players(Carlsern=2800, Shumaher=2900)



