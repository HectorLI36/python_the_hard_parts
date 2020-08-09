
# create a new type
class A(type):
    pass


class B(object, metaclass=A):
    pass


class C(B):
    pass


print(A.__class__)
print(B.__class__)
print(C.__base__)
print(C.__bases__)
print(C.__mro__)
print(C.__class__)
c = C()
print(c.__class__)

class E:
    pass

class F(E):
    pass

class G(F):
    pass

print(E.__class__)
print(F.__class__)
print(G.__class__)

pass