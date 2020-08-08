

# class and instance
class Student:

    def __init__(self):
        self.name = 'Hector'
        self.score = 100
        print('Student inited！')
    pass


def show_class_and_instance():
    a = Student
    b = Student()

    def print_score(student_obj):
        print(student_obj.score)

    print_score(b)
    pass


# three decorators
class A:

    bar = 'I am A'

    def __init__(self):
        self.self_bar = 'I am A init'

    def func_1(self):
        print('func_1')
        print(self.bar)

    @staticmethod
    def func_2():
        print('func_2')
        print(A.bar)

    @classmethod
    def func_3(cls):
        print('func_3')
        print(cls.bar)
        cls.func_2()
        A().func_1()
        cls().func_1()

    @property
    def func_4(self):
        print('func_4')
        print(self.bar)
        return self.self_bar  # check

    # x = property(g, s, d, doc)


def show_three_decorators():
    A().func_1()
    # A.func_1()

    A().func_2()
    A.func_2()

    A().func_3()
    A.func_3()

    # a = A.func_4()
    a = A.func_4
    a = A().func_4
    # a = A.func_4()


if __name__ == '__main__':
    show_class_and_instance()
    show_three_decorators()
