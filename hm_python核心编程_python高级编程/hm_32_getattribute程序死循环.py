class Person(object):
    def __getattribute__(self, obj):
        print("---test---")
        if obj.startswith("a"):
            return "hahha"
        else:
            return self.test  # 直接循环调用def __getattribute__


    def test(self):
        print("heihei")


t = Person()
print(t.a)
# print(t.b) # 会让程序死循环