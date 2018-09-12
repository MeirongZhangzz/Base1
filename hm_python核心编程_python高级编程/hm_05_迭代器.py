# 迭代器(Iterator)是指可以被next()函数调用并不断返回下一个值得对象

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
# 　把list、dict、str等Iterable对象变成Iterator可以使用iter（）函数

# for a in "abc":
#     print (a)
#
# for temp in [11,22,33,44,55]:
#     print(temp)


# a = (x for x in range(10))
# print(a)
# for tempe in a:
#     print(tempe)


# from collections import Iterable
#
# print(isinstance("abc",Iterable))
# print(isinstance([],Iterable))
# print(isinstance({},Iterable))
# print(isinstance(int,Iterable))

from collections import Iterator

print(isinstance("abc", Iterator))

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
# 　把list、dict、str等Iterable对象变成Iterator可以使用iter（）函数
print(isinstance([], Iterator))
print(isinstance(iter([]), Iterator))
