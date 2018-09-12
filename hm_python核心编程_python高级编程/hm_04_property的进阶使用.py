class Test(object):

    def __init__(self):
        self.__num = 100

    @property
    def num(self):
        print("-----getter-----")
        return self.__num

    @num.setter
    def num(self,newNum):
        print("-----setter-----")
        self.__num = newNum


t = Test()
# 相当于调用了 t.setNum(200)
t.num = 200
# 相当于调用了 t.getNum()
print(t.num)