import types


class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

    def eat(self):
        print("----%s正在吃----" % self.name)


def run(self):
    print("----%s正在跑----" % self.name)


p1 = Person("p1", 18)
p1.eat()

# 虽然p1对象中run属性已经指向了11行的run函数，但是这句代码还不正确
# 因为run属性指向的函数，是后来添加的，p1.run（）的时候，并没有把p1
# 当作第一个参数，导致了第11行函数调用的时候，出现缺少参数的问题
# p1.run = run
# p1.run
p1.run = types.MethodType(run, p1)
p1.run()

# 实例方法同对象绑定，静态或者类方法同类绑定
P = Person


@staticmethod
def talk():
    print("----static method----")


P.talk = talk
P.talk()

P.xx = talk
P.xx()


@classmethod
def printNum(cls):
    print("----class method----")


P.printNum = printNum
P.printNum()

P.xx = printNum
P.xx()