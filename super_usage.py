#实例一：
class A(object):
    def __init__(self):
        print("class ---- A ----")

class B(A):
    def __init__(self):
        print("class ---- B ----")
        super(B, self).__init__()

class C(A):
    def __init__(self):
        print("class ---- C ----")
        # print(f'printing {i}')
        super(C, self).__init__()
#
# class D(B, C):
#     def __init__(self):
#         print("class ---- D ----")
#         super(D, self).__init__()
#
#
# #实例二： 更改一下类D的super函数：
# class D(B, C):
#     def __init__(self):
#         print("class ---- D ----")
#         super(B, self).__init__()

class D(B, C):
    def __init__(self):
        print("class ---- D ----")
        super(D, self).__init__()

d = D()
pass