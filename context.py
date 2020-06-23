
class Withed:
    def __init__(self, whoami):
        self.foo = whoami

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            print(f'exiting {self.foo}')
            self.method_b()
        except AttributeError:
            print('cannot close')
        return True

    def method_a(self):
        print('method A called')

    def method_b(self):
        print('method B called')


def bar():
    with Withed('iamwithed') as w:
        w.method_a()


if __name__ == '__main__':
    bar()
