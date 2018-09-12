def w1(func):
    def inner():
        print("---正在验证---")
        if False:
            func()
        else:
            print("没有权限")
    return inner

# 等效于f1 = w1(f1)
@w1
def f1():
    print("---f1---")

@w1
def f2():
    print("---f2---")

# innerFunc = w1(f1)
# innerFunc()

# f1 = w1(f1)
f1()
f2()