# # old school ways
# class Base:
#     def __init__(self):
#         print('Base.__init__')
#
# class A(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('A.__init__')
#
# class B(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('B.__init__')
#
# class C(A,B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         print('C.__init__')
#
# # this gonna work
# A()
#
# # but this is not we expected
# C()

# ***************************************************
# here comes super
class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')

class C(A,B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C.__init__')


C()