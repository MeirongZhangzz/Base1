class Person(object):
    __slots__ = ("name", "age")  # 限定类对象的属性只有name和age


p = Person()
p.name = "小明"
p.age = 18
p.addr = "beijing"