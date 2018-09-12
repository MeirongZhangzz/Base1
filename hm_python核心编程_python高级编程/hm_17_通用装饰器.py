def func(functionName):
    def func_in(*args, **kwargs):
        print("---记录日志---")
        ret = functionName(*args, **kwargs)
        return ret

    return func_in


# 有返回值的函数
@func
def dtest():
    print("---dtest---")
    return "haha"


# 无返回值的函数
@func
def dtest2():
    print("---dtest2---")


# 带参数的函数
@func
def dtest3(a):
    print("---dtest3--a=%d---" % a)


ret = dtest()
print("dtest return value is %s" % ret)

a = dtest2()
print("dtest2 return value is %s" % a)

dtest2()
dtest3(11)