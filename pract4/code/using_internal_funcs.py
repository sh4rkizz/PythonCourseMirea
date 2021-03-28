class UserClass:
    def __init__(self):
        self.string = 'i`m just a useless string'
        self.tup = ('Very', 'interesting', 'personalities')
        self.number = 2468

    def to_string(self):
        return f'string = {self.string}\n' \
               f'tup = {self.tup}\n' \
               f'number = {self.number}'


if __name__ == '__main__':
    print(vars(UserClass()))
    print(UserClass().__dict__)
    print(UserClass().to_string())
