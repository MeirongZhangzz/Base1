# 斐波那契数列(Fibonacci)：除第一个和第二个数外，任意一个数都可由前两个数相加得到
def creatNum():
    print("---start---")
    a,b = 0,1
    for i in range(5):
        print("---1---")
        yield b
        # print(b)
        print("---2---")
        a,b = b,a+b
        print("---3---")
    print("---stop")

# 创建一个生成器对象
c = creatNum()

for num in c:
    print(num)

# ret = c.__next__()
# print(ret)
# 注意：
# next(c)
# c.__next__()
# 以上两种方式是一样的

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
