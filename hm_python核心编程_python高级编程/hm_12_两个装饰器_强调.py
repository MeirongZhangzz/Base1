def w1(func):
    def inner():
        print("---正在验证1---")
        func()
    return inner


def w2(func):
    def inner():
        print("---正在验证2---")
        func()
    return inner


@w1
@w2
def f1():
    print("---1---")

# @w1
# def f2():
#     print("---2---")

f1()

# f2()