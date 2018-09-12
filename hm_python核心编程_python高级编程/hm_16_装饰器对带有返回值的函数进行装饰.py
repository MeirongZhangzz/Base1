def func(functionName):
    print("---func---1----")

    def func_in():
        print("---func_in---1---")
        ret = functionName()  # 保存返回来的haha
        print("---func_in---2---")
        return ret  # 把haha返回到19行处的调用

    print("---func---2---")
    return func_in


@func
def dtest():
    print("---dtest---")
    return "haha"


ret = dtest()
print("dtest return value is %s" % ret)