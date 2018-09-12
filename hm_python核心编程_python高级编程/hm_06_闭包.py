# 定义一个函数
def dtest(number):
    print("--1--")

    # 在函数内部再定义一个函数，并且这个函数用到了外边函数的变量,那么将这个函数以及用到的一些变量称之为闭包
    def dtest_in(number2):
        print("--2--")
        print(number+number2)
        # 这里返回的就是闭包的结果

    print("--3--")
    return dtest_in


ret = dtest(100)
print("-" * 30)
ret(1)
# ret(100)
# ret(200)
