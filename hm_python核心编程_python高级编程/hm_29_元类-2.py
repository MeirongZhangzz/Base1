class Animal(object):
    def eat(self):
        print("-----eat-----")
# 1
class Dog(Animal):
    pass


wangcai = Dog()
wangcai.eat()


#  同1等效
Cat = type("Cat",(Animal,),{})
Xiaohuamao = Cat()
Xiaohuamao.eat()

# 查询创建关系
print(Cat.__class__)
print(Xiaohuamao.__class__)
print(type.__class__)