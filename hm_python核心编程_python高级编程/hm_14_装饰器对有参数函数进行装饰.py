def func(functionName):
    print("---func---1----")

    def func_in(a, b):
        print("---func_in---1---")
        functionName(a, b)
        print("---func_in---2---")

    print("---func---2---")
    return func_in


@func
def dtest(a, b):
    print("---dtest---a=%d,b=%d---" % (a, b))


dtest(11, 22)