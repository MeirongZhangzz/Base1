# LEGB顺序原则，locals->enclosing function->globals->builtins(内建)
num = 100  # globals变量


def test1():
    num = 200  # enclosing function

    def test2():
        num = 300  # locals变量
        print(num)

    return test2


ret = test1()
ret()