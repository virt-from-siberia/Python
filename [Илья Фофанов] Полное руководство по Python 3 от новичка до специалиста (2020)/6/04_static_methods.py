class StaticTest:
    x = 1


t1 = StaticTest()

print(f'Via instance : {t1.x}')
print(f'Via class : {StaticTest.x}')

t1.x = 2

print(f'Via instance : {t1.x}')
print(f'Via class : {StaticTest.x}')

StaticTest.x = 3

print(f'Via instance : {t1.x}')
print(f'Via class : {StaticTest.x}')


class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def display(self):
        return f'{self.month}--{self.day}--{self.year}'

    @classmethod
    def millenium_c(cls, month, day):
        return cls(month, day, 2000)

    @staticmethod
    def millenium_s(month, day):
        return Date(month, day, 2000)


D1 = Date.millenium_c(6, 9)
D2 = Date.millenium_s(6, 9)

print(D1.display())
print(D2.display())


class DateTime(Date):
    def display(self):
        return f'{self.month}--{self.day}--{self.year} - 00:00:00PM'


DT1 = DateTime(10, 10, 1990)
DT2 = DateTime.millenium_s(10, 10)

print(isinstance(DT1, DateTime))
print(isinstance(DT2, DateTime))
print(isinstance(DT2, Date))

print(DT1.display())
print(DT2.display())


class StrConverter:

    @staticmethod
    def to_str(bytes_or_str):
        if isinstance(bytes_or_str, bytes):
            value = bytes_or_str.decode('utf8')
        else:
            value = bytes_or_str
        return value

    @staticmethod
    def to_bytes(bytes_or_str):
        if isinstance(bytes_or_str, str):
            value = bytes_or_str.encode('utf8')
        else:
            value = bytes_or_str
        return value


print(StrConverter.to_str('\x41'))
print(StrConverter.to_str('A'))

print(StrConverter.to_bytes('\x41'))
print(StrConverter.to_bytes('A'))
