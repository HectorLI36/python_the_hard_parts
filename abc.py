import abc
import six


@six.add_metaclass(abc.ABCMeta)
class BaseClass(object):
    @abc.abstractmethod
    def func_a(self, data):
        """
        an abstract method need to be implemented
        """

    @abc.abstractmethod
    def func_b(self, data):
        """
        another abstract method need to be implemented
        """

class SubclassImpl(BaseClass):  # 不行
    def func_a(self, data):
        print("Overriding func_a, " + str(data))

    @staticmethod
    def func_d(self, data):
        print(type(self) + str(data))

class RegisteredImpl(object):  # 可以不实现
    @staticmethod
    def func_c(data):
        print("Method in third-party class, " + str(data))

BaseClass.register(RegisteredImpl)


if __name__ == '__main__':
    for subclass in BaseClass.__subclasses__():
        print("subclass of BaseClass: " + subclass.__name__)
    print("subclass do not contains RegisteredImpl")
    print("-----------------------------------------------")

    print("RegisteredImpl is subclass: " + str(issubclass(RegisteredImpl, BaseClass)))
    print("RegisteredImpl object  is instance: " + str(isinstance(RegisteredImpl(), BaseClass)))
    print("SubclassImpl is subclass: " + str(issubclass(SubclassImpl, BaseClass)))

    print("-----------------------------------------------")
    obj1 = RegisteredImpl()
    obj1.func_c("RegisteredImpl new object OK!")
    print("-----------------------------------------------")
    obj2 = SubclassImpl()  #由于没有实例化所有的方法，所以这里会报错 Can't instantiate abstract class SubclassImpl with abstract methods func_b
    obj2.func_a("It's right!")

"""
subclass of BaseClass: SubclassImpl
subclass do not contains RegisteredImpl
-----------------------------------------------
RegisteredImpl is subclass: True
RegisteredImpl object  is instance: True
SubclassImpl is subclass: True
-----------------------------------------------
Method in third-party class, RegisteredImpl new object OK!
-----------------------------------------------
Traceback (most recent call last):
  File "/Users/wangqi/Git/Python/scrapy_crawler_learn/test/ABCTest.py", line 51, in <module>
    obj2 = SubclassImpl()  #由于没有实例化所有的方法，所以这里会报错 Can't instantiate abstract class SubclassImpl with abstract methods func_b
TypeError: Can't instantiate abstract class SubclassImpl with abstract methods func_b
————————————————
"""