# 斐波那契数列(Fibonacci)：除第一个和第二个数外，任意一个数都可由前两个数相加得到
def creatNum():
    print("---start---")
    a,b = 0,1
    for i in range(5):
        print("---1---")
        yield b
        print(b)
        print("---2---")
        a,b = b,a+b
        print("---3---")
    print("---stop")


# 或者在Terminal里面run，将code copy进Terminal run

# c = creatNum()
# next(c)
# next(c)
# next(c)
# next(c)
# next(c)
# next(c)
# next(c)
# next(c)


# def creatNum():
#     print("---start---")
#     a,b = 0,1
#     for i in range(5):
#         print(b)
#         a,b = b,a+b
#     print("---stop")
#
#
# creatNum()
