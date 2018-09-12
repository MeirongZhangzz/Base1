class Test(object):

    def __init__(self):
        self.__num = 100

    def setNum(self,newNum):
        print("-----setter-----")
        self.__num = newNum

    def getNum(self):
        print("-----getter-----")
        return self.__num

    num = property(getNum , setNum)


t = Test()
# print(t.__num)
# t.__num = 200

# print(t.getNum())
# t.setNum(50)
# print(t.getNum())

print("-"*50)

t.num = 200
print(t.num)