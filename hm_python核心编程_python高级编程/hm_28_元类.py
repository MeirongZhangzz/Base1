# 类也是对象
class Person(object):
    num = 100

    print("---person---test---")

    def __init__(self):
        self.name = "abc"


print(100)
print("hello")
print(Person)

print("---type---动态创建类---")


# type动态的创建类
class Test1(object):
    pass


p1 = Test1()
Test2 = type("Test2", (), {})
p2 = Test2()
print(type(p1))
print(type(p2))

print("---type---动态创建类属性---")


class Test3(object):
    num = 0


Person2 = type("Person2", (), {"num": 0})
p3 = Test3()
p4 = Person2()
print(p3.num)
print(p4.num)

print("---type---动态创建类方法---")


def printNum(self):
    print("---num--%d---" % self.num)


Test4 = type("Test4", (), {"printNum": printNum})
t1 = Test4()
t1.num = 100
t1.printNum()

print("---type---动态创建类方法---等效方法---")


class printNum2(object):
    def printNum2(self):
        print("---num--%d---" % self.num)


t2 = printNum2()
t2.num = 100
t2.printNum2()
