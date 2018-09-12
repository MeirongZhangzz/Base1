def func(functionName):
    print("---func---1----")

    def func_in(*args, **kwargs):  # 如果a,b没有定义，会导致20行的调用失败
        print("---func_in---1---")
        functionName(*args, **kwargs)  # 如果没有把a,b当作实参进行传递，那么会导致调用13行的函数失败
        print("---func_in---2---")

    print("---func---2---")
    return func_in


@func
def dtest(a, b):
    print("---dtest---a=%d,b=%d---" % (a, b))


@func
def dtest1(a, b, c, d):
    print("---dtest---a=%d,b=%d,c=%d,d=%d---" % (a, b, c, d))


dtest(11, 22)
dtest1(44, 55, 66, 77)