greeting = 'hello from the global scope'


def greet():
    # greeting = 'hello from enclosing scope'

    def nexted():
        # greeting = 'hello from local scope'
        print(greeting)

    nexted()


greet()
print(greeting)

greeting = 'hello from the global scope'


def greet():
    global greeting
    print(f'Greet in func: {greeting}')

    greeting = 'Hello from enclosing scope'
    print(f'Greet in func: {greeting}')

    def nested():
        greeting = 'Hello from local scope'
        print(greeting)

    nested()


greet()
print(greeting)
